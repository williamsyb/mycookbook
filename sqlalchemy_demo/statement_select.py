# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 13:40
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : statement_select.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import or_

db_uri = 'sqlite:///db3.sqlite'
engine = create_engine(db_uri)
conn = engine.connect()

meta = MetaData(engine).reflect()
table = meta.tables['user']

# select * from 'user'
select_st = select([table]).where(
   table.c.l_name == 'Hello')
res = conn.execute(select_st)
for _row in res:
    print(_row)

# or equal to
select_st = table.select().where(
   table.c.l_name == 'Hello')
res = conn.execute(select_st)
for _row in res:
    print(_row)

# combine with "OR"
select_st = select([
   table.c.l_name,
   table.c.f_name]).where(or_(
      table.c.l_name == 'Hello',
      table.c.l_name == 'Hi'))
res = conn.execute(select_st)
for _row in res:
    print(_row)

# combine with "ORDER_BY"
select_st = select([table]).where(or_(
      table.c.l_name == 'Hello',
      table.c.l_name == 'Hi')).order_by(table.c.f_name)
res = conn.execute(select_st)
for _row in res:
    print(_row)