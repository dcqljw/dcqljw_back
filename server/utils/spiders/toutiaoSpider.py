import datetime
import hashlib

import requests
from utils.spiders.save_spider_data.hot_save_data import save

def run():
    url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00901qxmDMgAAIDDz2zMoFRAZbasQghAAM.KmnOBANzrvjmEPBDt1kuEvBYEU0O.g1Rh4FDeb-TsRWNNTasLytaOqUS9qO2Zh61DjImrm.krAADpPzyNIrYFvik1TC5PB00iIbbd98"

    response = requests.get(url)

    res_text = response.json()

    spider_type = "toutiao"
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_date)
    spider_id = hashlib.md5(f"{spider_type}{now_date}".encode("utf-8")).hexdigest()
    print(spider_id)
    items = res_text['data']
    insert_data = []
    for i in items:
        note = i['Title']
        insert_data.append(
            (spider_id, spider_type, note, now_date, str(i))
        )
    print(insert_data)
    save(insert_data=insert_data, spider_type=spider_type, now_date=now_date, spider_id=spider_id)
