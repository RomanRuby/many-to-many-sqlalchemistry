# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from backend.models import Base
from backend.models.PersonItemEntity import PersonItemEntity
from .Entity import Entity


class PersonEntity(Entity, Base):
    __tablename__ = 'persons'

    name = Column(String)
    items = relationship('ItemEntity', secondary="person_item", viewonly=True)

    def __init__(self, name):
        Entity.__init__(self)
        self.name = name
        self.items = []

    def addPersons(self, score):
        self.tag_issues.append(PersonItemEntity(expertise=self, score=score))


class PersonEntitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    items = fields.Str()
