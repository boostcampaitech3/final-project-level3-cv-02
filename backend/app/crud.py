from sqlalchemy.orm import Session

from . import models, schemas

# FE에서 DATA 받아올 때
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email, 
        original_img=user.original_img, 
        sketch_img=user.sketch_img
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# DB에 output_img 저장
def create_result(db: Session, user: schemas.UserCreate):
    db_result = models.User(output_img=user.output_img)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

