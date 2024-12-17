from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.orm import relationship

from ..common.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    email = Column(String, unique=True)
    password = Column(String)
    surname = Column(String)
    name = Column(String)
    patr = Column(String)

    is_admin = Column(Boolean, default=False)
    