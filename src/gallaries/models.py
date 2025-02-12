from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.orm import relationship

from ..common.database import Base


class Gallery(Base):
    __tablename__ = "gallaries"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    visible = Column(Boolean, default=True)

    