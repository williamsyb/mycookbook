# -*- coding UTF-8 -*-
# @project : python_web
# @Time    : 2020/7/15 12:29
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : load_from_existing_db.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

# Create a MetaData instance
metadata = MetaData()
print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print(metadata.tables)
