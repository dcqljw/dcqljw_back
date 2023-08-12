import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save
from pyquery import PyQuery as pq


def run():
    url = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/?reflow_source=reflow_page"

    response = requests.get(url)

    res_text = response.json()

    spider_type = "douyin"
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_date)
    spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
    print(spider_id)
    items = res_text['word_list']
    insert_data = []
    for i in items:
        note = i['word']
        insert_data.append(
            (spider_id, spider_type, note, now_date, str(i))
        )
    print(insert_data)
    save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
