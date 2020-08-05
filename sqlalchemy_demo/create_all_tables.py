from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)
meta = MetaData(engine)

# Register t1, t2 to metadata
t1 = Table('EX1', meta,
           Column('id', Integer, primary_key=True),
           Column('name', String))

t2 = Table('EX2', meta,
           Column('id', Integer, primary_key=True),
           Column('val', Integer))
# Create all tables in meta
meta.create_all()
