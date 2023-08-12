import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save


def run():
    url = "https://weibo.com/ajax/side/hotSearch"

    response = requests.get(url)

    res = response.json()
    realtime_ = res["data"]["realtime"]
    spider_type = "weibo"
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_date)
    spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
    print(spider_id)

    insert_data = []
    for source_data in realtime_:
        note = source_data["note"]
        insert_data.append(
            (spider_id, spider_type, note, now_date, str(source_data))
        )

    save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
