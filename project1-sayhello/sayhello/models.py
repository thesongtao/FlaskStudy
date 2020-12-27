#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:14
# @Author  : 君去不知何时归
# @Site    : 
# @File    : models.py
# @Desc:
from datetime import datetime
from sayhello import db
class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime,default=datetime.now,index=True)#传入的是方法对象,而不是执行结果。

