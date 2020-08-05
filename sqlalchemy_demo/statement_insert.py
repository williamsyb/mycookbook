# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 13:36
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : statement_insert.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

db_uri = 'sqlite:///db3.sqlite'
engine = create_engine(db_uri)

# create table
meta = MetaData(engine)
table = Table('user', meta,
              Column('id', Integer, primary_key=True),
              Column('l_name', String),
              Column('f_name', String))
meta.create_all()

# insert data via insert() construct
ins = table.insert().values(
    l_name='Hello',
    f_name='World')
conn = engine.connect()
conn.execute(ins)

# insert multiple data
conn.execute(table.insert(), [
    {'l_name': 'Hi', 'f_name': 'bob'},
    {'l_name': 'yo', 'f_name': 'alice'}])
