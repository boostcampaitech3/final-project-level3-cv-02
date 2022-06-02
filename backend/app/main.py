import base64
import os
import re
import shutil
import smtplib
from datetime import datetime
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

import aiofiles
import torch
import uvicorn
from dotenv import load_dotenv
from fastapi import (BackgroundTasks, FastAPI, File, Form, Request, Response,
                     UploadFile)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
from fastapi.responses import FileResponse, JSONResponse
from google.cloud import storage
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from . import api, crud, models, schemas
from .database import SessionLocal, engine, get_db

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
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/')
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


@app.get("/")
def get_user(db: Session = Depends(get_db)):
    result = db.query(models.User).all()

    # Cloud Storage
    bucket = client.bucket('bucket-interior')
    #blob = bucket.blob('images/')
    #blob.download_to_filename(IMG_DIR+'/output-2.jpg')

    return {"data": result}



## frontend에서 데이터 받아오기
@app.post('/')
async def get_form(request: Request, db: Session = Depends(get_db)):
    file_url = "https://storage.cloud.google.com/bucket-interior/images/" 

    loading = True
    item = await request.form()

    email = item['submit_email']
    name = get_username(email)

    original_img = item['submit_original_img']
    original_img_name = 'original_' + item['submit_original_img'].filename
    sketch_img = item['submit_sketch_img']
    sketch_img_name = 'sketch_' +item['submit_sketch_img'].filename
    original_img_width = item['original_image_width']
    original_img_height = item['original_image_height']
    sketch_img_width = item['sketch_image_width']
    sketch_img_height = item['sketch_image_height']
    timestamp = item['upload_time']

    # unique한 user dir 만들기
    user_name = name + '_' + str(timestamp)
    user_dir = os.path.join(IMG_DIR, user_name)
    os.makedirs(user_dir)

    # local path # await 로 보내기 
    file_location_o = os.path.join(user_dir, original_img_name)
    file_location_s = os.path.join(user_dir, sketch_img_name)

    # download to local
    async with aiofiles.open(file_location_o, "wb") as buffer:
        img = await original_img.read()
        await buffer.write(img)
    async with aiofiles.open(file_location_s, "wb") as buffer:
        img2 = await sketch_img.read()
        await buffer.write(img2)
    
    bucket = client.bucket('bucket-interior')
    blob_o = bucket.blob(os.path.join(os.path.join('images/', user_name), original_img_name))
    blob_s = bucket.blob(os.path.join(os.path.join('images/', user_name), sketch_img_name))

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
    user.name = user_name
    user.original_img = file_url + original_img_name
    user.sketch_img = file_url + sketch_img_name
    user.original_img_width = original_img_width
    user.original_img_height = original_img_height
    user.sketch_img_width = sketch_img_width
    user.sketch_img_height = sketch_img_height
    user.timestamp = timestamp

    result = crud.create_user(db=db, user=user)

    # To-Do
    # inference

    # To-Do
    #if output:
    #    send_email(email)

    #send_email(email)

    return result

def get_username(email):
    name = email.split('@')
    return name[0]

def send_email(email):
    msg = MIMEMultipart('alternative')

    email_sender=os.environ.get("EMAIL_SENDER")
    email_password=os.environ.get("EMAIL_PASSWORD")

    smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_gmail.ehlo()
    smtp_gmail.starttls()
    smtp_gmail.login(email_sender, email_password)

    msg['Subject']="💌 내일의 집이 도착했습니다!"
    msg['From']='버킷인테리어'
    msg['To']=email
    
    html_file = open(os.path.join(TEMPLATE_DIR,'email.html'))
    temp = MIMEText(html_file.read(), 'html')

    msg.attach(temp)

    smtp_gmail.send_message(msg,email_sender,email)
    print("발송완료!")
    smtp_gmail.quit()


