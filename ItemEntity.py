# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Text, Integer, ForeignKey, Float

from backend.models import Base
from backend.models.PersonItemEntity import PersonItemEntity
from .Entity import Entity
from sqlalchemy.orm import relationship


class ItemEntity(Entity, Base):
    __tablename__ = 'items'

    name = Column(String)
    item_score = Column(Float)
    persons_id = relationship("PersonEntity", secondary="person_item", viewonly=True)

    def __init__(self, name, score):
        Entity.__init__(self)
        self.name = name
        self.item_score = score
        self.persons_id = []


class ItemEntitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    score = fields.Number()
    persons_id = fields.Number()
