#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:15
# @Author  : 君去不知何时归
# @Site    : 
# @File    : settings.py
# @Desc:
import os
from sayhello import app
dev_db = "sqlite:///" + os.path.join(os.path.dirname(app.root_path),"data.db")
# 动态追踪修改设置，
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 查询时会显示原始sql 语句
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI",dev_db)
SECCRET_KEY = os.getenv('SECRET_KEY','secret string')
