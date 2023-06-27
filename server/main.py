import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models import models
from database import engine
from app.home import api as home_api
from fastapi import Request

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# @app.middleware('http')
# async def header_auth(request: Request, call_next):
#     dcq = request.headers.get('dcq', None)
#     if dcq != "5d9c9e023a33a510e7382393e7286d59":
#         return JSONResponse(status_code=404, content={"msg": "error"})
#     response = await call_next(request)
#     print(response)
#     return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
app.include_router(home_api.router)


@app.get("/")
def read_root():
    return {"code": "200"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
