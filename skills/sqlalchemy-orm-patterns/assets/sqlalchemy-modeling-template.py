from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ExampleParent(Base):
    __tablename__ = "example_parent"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    children = relationship("ExampleChild", back_populates="parent")


class ExampleChild(Base):
    __tablename__ = "example_child"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("example_parent.id"), nullable=False)

    parent = relationship("ExampleParent", back_populates="children")
