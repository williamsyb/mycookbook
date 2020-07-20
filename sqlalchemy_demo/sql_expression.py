# Think Column as "ColumnElement"
# Implement via overwrite special function
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import or_

meta = MetaData()
table = Table('example', meta,
              Column('id', Integer, primary_key=True),
              Column('l_name', String),
              Column('f_name', String))
# sql expression binary object
print(table.c.l_name == 'ed')
print(table.c.l_name.name)
print(repr(table.c.l_name == 'ed'))
# exhbit sql expression
print(str(table.c.l_name == 'ed'))

print(repr(table.c.f_name != 'ed'))
print('-------------------------------')
# comparison operator
print(repr(table.c.id > 3))
print('-------------------------------')
# or expression
print((table.c.id > 5) | (table.c.id < 2))
# Equal to
print(or_(table.c.id > 5, table.c.id < 2))
print('-------------------------------')
# compare to None produce IS NULL
print(table.c.l_name == None)
# Equal to
print(table.c.l_name.is_(None))
print('-------------------------------')
# + means "addition"
print(table.c.id + 5)
# or means "string concatenation"
print(table.c.l_name + "some name")
print('-------------------------------')
# in expression
print(table.c.l_name.in_(['a', 'b']))
