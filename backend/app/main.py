import base64
import os
import re
import shutil
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

import torch
import uvicorn
from fastapi import FastAPI, File, Request, Response, UploadFile, Form, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
from fastapi.responses import FileResponse
from google.cloud import storage
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from . import api, crud, models, schemas
from .database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import aiofiles


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
load_dotenv()

client = storage.Client()
loading = False

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ========================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'static/')
SERVER_IMG_DIR = os.path.join('gs://bucket-interior/','images/')

# GCS private key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# ===================================================================
# TODO : origin_img, sketch_img 입력
# TODO : 입력받은 두 이미지 출력
# TODO : email 주소 입력
# TODO : 제출 버튼 클릭
    # TODO : DB - origin_img, sketch_img, email, output_img, user_id
# TODO : model 돌림
# TODO : 결과 - email로 보냄
# ===================================================================
   
@app.get("/")
def get_user(db: Session = Depends(get_db)):
    result = db.query(models.User).all()

    # Cloud Storage
    #bucket = client.bucket('bucket-interior')
    #blob = bucket.blob('images/bedroom-9-1.jpg')
    #blob.download_to_filename(IMG_DIR+'/output-2.jpg')

    return {"data": result}



## frontend에서 데이터 받아오기
@app.post('/')
async def get_form(request: Request, db: Session = Depends(get_db)):
    file_url = "https://storage.cloud.google.com/bucket-interior/" 

    loading = True
    item = await request.form()

    email = item['submit_email']
    original_img = item['submit_original_img']
    original_img_name = item['submit_original_img'].filename
    sketch_img = item['submit_sketch_img']
    sketch_img_name = item['submit_sketch_img'].filename

    # local path
    file_location_o = os.path.join(IMG_DIR, original_img_name)
    file_location_s = os.path.join(IMG_DIR, sketch_img_name)

    # download to local
    async with aiofiles.open(file_location_o, "wb") as buffer:
        img = await original_img.read()
        await buffer.write(img)
    async with aiofiles.open(file_location_s, "wb") as buffer:
        img2 = await sketch_img.read()
        await buffer.write(img2)
    
    bucket = client.bucket('bucket-interior')
    blob_o = bucket.blob(os.path.join('images/', original_img_name))
    blob_s = bucket.blob(os.path.join('images/', sketch_img_name))

    # upload to bucket
    blob_o.upload_from_filename(file_location_o)
    blob_s.upload_from_filename(file_location_s)


    result={'OriginalImgName': original_img_name,
            'SketchImgName': sketch_img_name,
            'OriginalImgLocation' : file_url + original_img_name,
            'SketchImgLocatoion': file_url + sketch_img_name,
            'email': email}

    print(result)


    ## DB에 저장하기
    user = schemas.UserCreate
    user.email = email
    user.original_img = file_url + original_img_name
    user.sketch_img = file_url + sketch_img_name

    result = crud.create_user(db=db, user=user)

    return result










