#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-05 19:37
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : author.py
# @Desc: 用户管理蓝本
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import request,Blueprint,render_template
user_bp = Blueprint("author",__name__)

@user_bp.route("/login/",methods=["GET","POST"])
def login():
    pass
