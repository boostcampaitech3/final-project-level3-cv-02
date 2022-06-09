from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    Float
)
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, default=False)
    original_img = Column(String)
    sketch_img = Column(String)
    output_img = Column(String)
    original_img_width = Column(Integer)
    original_img_height = Column(Integer)
    sketch_img_width = Column(Integer)
    sketch_img_height = Column(Integer)
    timestamp = Column(String)