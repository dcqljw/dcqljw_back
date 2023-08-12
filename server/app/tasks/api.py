from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import APIRouter

from utils.spiders import baiduSpider

router = APIRouter(prefix='/task')
scheduler = AsyncIOScheduler()

tasks_list = []


async def test_task(task_name: str):
    baiduSpider.run()
    print("开始运行百度爬虫")


@router.get("/add_job")
async def add_job(task_name: str):
    scheduler.add_job(test_task, "interval", seconds=5, id=task_name, args=[task_name])
    return {"msg": "添加成功"}


@router.get("/start_job")
async def start_job():
    scheduler.start()
    return {"msg": "开始运行"}


@router.get("/get_job_status")
async def get_job_status(task_id: str):
    status = scheduler.get_job(task_id)
    print(status)
    return {"msg": status.next_run_time}


@router.get("/pause_job")
async def pause_job(task_id: str):
    job = scheduler.pause_job(task_id)
    print(job)
    return {"msg": "暂停成功"}
