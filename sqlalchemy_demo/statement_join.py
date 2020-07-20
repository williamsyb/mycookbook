# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 13:42
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : statement_join.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select

db_uri = 'sqlite:///db3.sqlite'
engine = create_engine(db_uri)

meta = MetaData(engine).reflect()
email_t = Table('email_addr', meta,
                Column('id', Integer, primary_key=True),
                Column('email', String),
                Column('name', String))
meta.create_all()

# get user table
user_t = meta.tables['user']

# insert
conn = engine.connect()
conn.execute(email_t.insert(), [
    {'email': 'ker@test', 'name': 'Hi'},
    {'email': 'yo@test', 'name': 'Hello'}])
# join statement
join_obj = user_t.join(email_t,
                       email_t.c.name == user_t.c.l_name)
# using select_from
sel_st = select(
    [user_t.c.l_name, email_t.c.email]).select_from(join_obj)
res = conn.execute(sel_st)
for _row in res:
    print(_row)
