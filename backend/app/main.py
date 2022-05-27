import base64
import os
import re
import shutil
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

import torch
import uvicorn
from fastapi import FastAPI, File, Request, Response, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
from fastapi.responses import FileResponse
from google.cloud import storage
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from . import api, crud, models, schemas
from .database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '[Key위치]'


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
    bucket = client.bucket('bucket-interior')
    blob = bucket.blob('images/bedroom-9-1.jpg')
    blob.download_to_filename(IMG_DIR+'/output-2.jpg')

    return {"data": result}

@app.post('/upload-images')
async def upload_image(in_file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_url = ''
    saved_file_name = in_file.filename
    file_url = "https://storage.cloud.google.com/bucket-interior/"

    # local path
    file_location = os.path.join(IMG_DIR, saved_file_name)

    # download to local
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(in_file.file, buffer)

    bucket = client.bucket('bucket-interior')
    blob = bucket.blob(os.path.join('images/',saved_file_name))
    print(saved_file_name)

    # upload to bucket
    blob.upload_from_filename(file_location)


    result={'fileName' : saved_file_name,
            'fileLocation' : file_url + saved_file_name}

    return result

'''
@app.get('/images/{file_name}')
async def get_image(file_name:str):
    return FileResponse(''.join([IMG_DIR,file_name]))

'''

## frontend에서 데이터 받아오기
@app.post('/')
async def get_form(request: Request):

    loading = True
    item = await request.form()
    data = item['submit_email']
    print(data)
    return {"email": data}










