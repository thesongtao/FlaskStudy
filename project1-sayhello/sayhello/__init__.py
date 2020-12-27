#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:13
# @Author  : 君去不知何时归
# @Site    : 
# @File    : __init__.py.py
# @Desc:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask('sayhello')
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
from sayhello import views,errors,commands
