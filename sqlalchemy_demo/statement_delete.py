# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 13:44
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : statement_delete.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import MetaData

db_uri = 'sqlite:///db3.sqlite'
engine = create_engine(db_uri)
conn = engine.connect()

meta = MetaData(engine).reflect()
user_t = meta.tables['user']

# select * from user_t
sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res:
    print(_row)

# delete l_name == 'Hello'
del_st = user_t.delete().where(
      user_t.c.l_name == 'Hello')
print('----- delete -----')
res = conn.execute(del_st)

# check rows has been delete
sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res:
    print(_row)