from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from datetime import datetime

class Image(BaseModel):
    width: int
    height: int

class UserCreate(BaseModel):
    id : int
    name : str
    email : EmailStr
    original_img : HttpUrl
    sketch_img : HttpUrl
    output_img : str = None
    original_img_width : int
    original_img_height : int
    sketch_img_width : int
    sketch_img_height : int
    timestamp : str

    class Config:
        orm_mode = True

