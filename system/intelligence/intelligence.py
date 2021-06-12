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
intelligence_bp = Blueprint("intelligence",__name__)

@intelligence_bp.route("/createreport/",methods = ["GET"])
def create_report():
    """
    生成年级成绩单
    """
    pid = request.args.get("parentid")
    subject_id = request.args.get("subjectid")
    sql = 'select * from t_knowledge_points_tree where parent_id=%s and subject_id=%s'%(pid,subject_id)
    print(sql)
    res = mysql.select(sql)
    print(res)
    dataList = []
    for tp in res:
        data = {
            "tree_id":None,
            "name":None,
            "parent_id":None,
            "is_have_childe":None,
            "subject_id":None,
        }
        tree_id = tp[0]
        name= tp[1]
        parent_id = tp[2]
        is_have_childe = tp[3]
        subject_id = tp[4]
        data["tree_id"] = tree_id
        data["name"] = name
        data["parent_id"] = parent_id
        data["is_have_childe"] = is_have_childe
        data["subject_id"] = subject_id
        dataList.append(data)
    return json.dumps(dataList)

