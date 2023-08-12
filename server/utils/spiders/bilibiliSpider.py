import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save


def run():
    url = "https://app.bilibili.com/x/v2/search/trending/ranking?limit=30"

    response = requests.get(url)

    res_text = response.json()

    spider_type = "bilibili"
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_date)
    spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
    print(spider_id)
    items = res_text['data']['list']
    insert_data = []
    for i in items:
        note = i['keyword']
        insert_data.append(
            (spider_id, spider_type, note, now_date, str(i))
        )
    print(insert_data)
    save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
