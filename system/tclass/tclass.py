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
class_bp = Blueprint("tclass",__name__)

@class_bp.route("/update/",methods = ["POST"])
def update_class():
    """
    修改班级,目前只允许修改班主任
    {
        "id":"3"
        "headteacher":"天秀儿"
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    headteacher = data.get("headteacher","")
    id = data.get("id")
    sql = 'update t_class set headteacher="%s"where id="%s"'%(headteacher,id)
    print(sql)
    res = mysql.insert(sql)
    return res

@class_bp.route("/select/",methods = ["GET"])
def select_class():
    """
    查询所有班级,也可查看指定年级班级
    :return:
    """
    headteacher= request.args.get("headteacher")
    level = request.args.get("level","")
    sql = "select * from t_class where 1=1"
    if level != "":
        sql += " and level=%s"%level
    if headteacher !="":
        sql += ' and headteacher="%s"'%(headteacher)
    res = mysql.select(sql)

    userList = []
    for tp in res:
        id = tp[0]
        level = tp[1]
        cno = tp[2]
        headteacher = tp[3]
        userList.append({
            "id":id,
            "level":level,
            "cno":cno,
            "headteacher":headteacher
        })
    return json.dumps(userList)

@class_bp.route("/delete/",methods = ["GET"])
def delete_class():
    """
    删除班级
    :return:
    {
        "id":2
    }
    """
    id = request.args.get("id")
    sql = "delete from t_class where id=%s"%(id)
    res = mysql.insert(sql)
    print(res)
    if res["result"] is True:
        return {
            "desc":"删除成功!"
        }
@class_bp.route("/create/",methods = ["POST"])
def create_class():
    """
    添加班级
    {
        "level":"2021",
        "cno":"3"
        "headteacher":"秀儿"
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    level = data.get("level","")
    cno = data.get("cno", "")
    headteacher = data.get("headteacher", "")
    if level == "" or cno =="" or headteacher == "":
        return {
            "desc":"所有字段均不允许为空!"
        }
    sql= 'select * from t_class where level = "%s" and cno="%s"'%(level,cno)
    print(sql)
    res = mysql.select(sql)
    if len(res) >0:
        return {
            "desc":"班级已存在,不可重复添加!"
        }
    else:
        sql = 'insert into t_class (level,cno,headteacher) values("%s","%s","%s")'%(level,cno,headteacher)
        res = mysql.insert(sql)
        return res


