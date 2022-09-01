#!/usr/bin/python3
"""Define class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Starting the class"""
    __tablename__ = 'states'
    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
