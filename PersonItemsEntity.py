# coding=utf-8

from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Float
from sqlalchemy.orm import sessionmaker, relationship, backref
from backend.models import Base
from .Entity import Entity


class PersonItemEntity(Entity, Base):
    __tablename__ = 'person_item'

    id = Column(Integer, Sequence('seq_reg_id', start=1, increment=1),
                primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)

    score = Column(Float)
    person = relationship("PersonEntity", backref=backref("person_items", cascade="all, delete-orphan"))
    item = relationship("ItemEntity", backref=backref("person_items", cascade="all, delete-orphan"))

    def __init__(self, item=None, score=0):
        Entity.__init__(self)
        self.score = score
        self.item = item
        self.person = self
