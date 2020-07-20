from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

meta = MetaData()
t = Table('ex_table', meta,
          Column('id', Integer, primary_key=True),
          Column('key', String),
          Column('val', Integer))
# Get Table Name
print('t.name:', t.name)

# Get Columns
print('t.columns.keys():', t.columns.keys())

# Get Column
c1 = t.c.key
print('t.c.key.name:', c1.name)
# Or
c2 = t.columns.val
print('t.columns.val.name:', c2.name)

# Get Table from Column
print(c1.table)
print(c2.table)
