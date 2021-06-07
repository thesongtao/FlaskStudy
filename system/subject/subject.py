#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 18:17
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : class.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Blueprint,request,current_app
from DBPool import MySQL
import json
mysql = MySQL()
subject_bp = Blueprint("subject",__name__)

@subject_bp.route("/select/",methods = ["GET"])
def select_subject():
    """
    学科类型查询
    """
    sql = 'select * from t_subject'
    print(sql)
    res = mysql.select(sql)
    print(res)
    dataList = []
    for tp in res:
        data = {
            "id":"",
            "name":""
        }
        id = tp[0]
        name= tp[1]
        data["id"] = str(id)
        data["name"] = name
        dataList.append(data)
    return json.dumps(dataList)

