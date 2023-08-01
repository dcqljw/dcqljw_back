import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save
from pyquery import PyQuery as pq


def run():
    try:
        url = "https://top.baidu.com/board?tab=realtime"

        response = requests.get(url)

        res_text = response.text
        doc = pq(res_text)

        items = doc(".category-wrap_iQLoo").items()
        spider_type = "baidu"
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now_date)
        spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
        print(spider_id)

        insert_data = []
        for i in items:
            note = i('.c-single-text-ellipsis').text()
            insert_data.append(
                (spider_id, spider_type, note, now_date, str(""))
            )

        save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
        return {"status": True}
    except Exception as e:
        return {"status": False, "msg": e}


if __name__ == '__main__':
    run()
