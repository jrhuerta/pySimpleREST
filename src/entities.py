__author__ = 'jrhuerta'

from datetime import datetime
from sqlalchemy import Column, Unicode, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'

    id = Column('SomethingElse', Integer, primary_key=True, autoincrement=True,
                nullable=False)
    title = Column(Unicode(255), nullable=False)
    published = Column(DateTime, nullable=False,
                       default=lambda: datetime.utcnow())
    active = Column(Boolean)
    views = Column(Integer)
