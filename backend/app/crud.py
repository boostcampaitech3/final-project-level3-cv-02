from sqlalchemy.orm import Session

from . import models, schemas


# FE에서 DATA 받아 올 때
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email, 
        original_img=user.original_img, 
        sketch_img=user.sketch_img,
        original_img_width=user.original_img_width,
        original_img_height=user.original_img_height,
        sketch_img_width=user.sketch_img_width,
        sketch_img_height=user.sketch_img_height,
        timestamp=user.timestamp
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# DB에 output_img 저장
def update_user(db: Session, user_name: str, output_img: str):
    db_user = db.query(models.User).filter(models.User.name == user_name).first()
    db_user.output_img = output_img
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
