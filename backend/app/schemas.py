from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field, HttpUrl

class Image(BaseModel):
    img_url: HttpUrl

class UserCreate(BaseModel):
    id : int
    email : EmailStr
    original_img : HttpUrl
    sketch_img : HttpUrl
    output_img : HttpUrl = None

    class Config:
        orm_mode = True