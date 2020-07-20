from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    String,
    Integer)

from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:///db2.sqlite"
engine = create_engine(db_url)

Base = declarative_base()


class TemplateTable(object):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class DowntownAPeople(TemplateTable, Base):
    __tablename__ = "downtown_a_people"


class DowntownBPeople(TemplateTable, Base):
    __tablename__ = "downtown_b_people"


Base.metadata.create_all(bind=engine)

# check table exists
ins = inspect(engine)
for _t in ins.get_table_names():
    print(_t)
