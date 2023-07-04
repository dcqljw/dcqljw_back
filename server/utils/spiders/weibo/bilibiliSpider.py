import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save

url = "https://api.bilibili.com/x/web-interface/wbi/search/square?limit=10&platform=web&w_rid=79e7d91a79a64fb6de5cebcf3cdb5f51&wts=1688488625"

response = requests.get(url)

res_text = response.json()

spider_type = "bilibili"
now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now_date)
spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
print(spider_id)
items = res_text['data']['trending']['list']
insert_data = []
for i in items:
    note = i['keyword']
    insert_data.append(
        (spider_id, spider_type, note, now_date, str(i))
    )
print(insert_data)
save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
