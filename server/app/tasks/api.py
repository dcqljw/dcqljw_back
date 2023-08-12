from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from utils.spiders import baiduSpider, bilibiliSpider, douyinSpider, toutiaoSpider, weiboSpider

router = APIRouter(prefix='/task')
scheduler = AsyncIOScheduler()

tasks_list = []


async def test_task(task_name: str):
    print("开始运行")
    baiduSpider.run()
    bilibiliSpider.run()
    douyinSpider.run()
    toutiaoSpider.run()
    weiboSpider.run()


@router.get("/add_job")
async def add_job(request: Request, task_name: str):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    await test_task("")
    scheduler.add_job(test_task, "interval", hours=1, id=task_name, args=[task_name])
    return {"msg": "添加成功"}


@router.get("/start_job")
async def start_job(request: Request):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    if not scheduler.running:
        scheduler.start()
        return {"msg": "开始运行"}
    else:
        return {"msg": "已经启动无需启动"}


@router.get("/get_job_status")
async def get_job_status(request: Request, task_id: str):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    status = scheduler.get_job(task_id)
    return {"msg": status.next_run_time}


@router.get("/pause_job")
async def pause_job(request: Request, task_id: str):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    job = scheduler.pause_job(task_id)
    print(job)
    return {"msg": "暂停成功"}
