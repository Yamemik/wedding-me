from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.orm import relationship

from ..common.database import Base


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    visible = Column(Boolean, default=True)
    
    user_id = Column()
    