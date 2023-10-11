import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.home import api as home_api
from app.tasks import api as tasks_api
from app.users import api as users_api
from app.groups import api as groups_api

# 不需要创建数据库
# models.Base.metadata.create_all(bind=engine)
# app = FastAPI(docs_url=None, redoc_url=None)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(home_api.router)
app.include_router(tasks_api.router)
app.include_router(users_api.router)
app.include_router(groups_api.router)


@app.get("/")
def read_root(data):
    return {"code": "200", "data": data}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
