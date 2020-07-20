# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 12:34
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : get_table_from_db.py
# @Software: PyCharm
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

# Create MetaData instance
metadata = MetaData()
metadata.reflect(bind=engine)
print(metadata.tables)

# Get Table
ex_table = metadata.tables['Example']
print(ex_table)