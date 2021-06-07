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
student_bp = Blueprint("student",__name__)

@student_bp.route("/update/",methods = ["POST"])
def update_student():
    """
    创建账号
    {
        "id":"3"
        "classid":"管理员1",
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    id = data.get("id","")
    cid = data.get("classid", "")
    sql = 'update t_student set classid=%s where id="%s"'%(cid,id)
    print(sql)
    res = mysql.insert(sql)
    return res

@student_bp.route("/select/",methods = ["GET"])
def select_all():
    """
    查询学生
    :return:
    """
    dataList = []
    all = request.args.get("all","")
    print("all:",all)
    sql = """
            select   t_student.id,
                     t_student.sname,
                     t_student.sno,
                     t_student.sex,
                     t_class.id as classid,
                     t_class.level,
                     t_class.cno,
                     t_class.headteacher
                            from t_student,t_class 
                            where t_student.classid=t_class.id and 1=1
            """
    if all != "":
        data = mysql.select(sql)
        for tp in data:
            d = {}
            id= tp[0]
            sname = tp[1]
            sno = tp[2]
            sex = tp[3]
            classid = tp[4]
            level = tp[5]
            cno = tp[6]
            headteacher=tp[7]
            d.update(id=id)
            d.update(sname=sname)
            d.update(sno=sno)
            d.update(sex=sex)
            d.update(classid=classid)
            d.update(level=level)
            d.update(cno=cno)
            d.update(headteacher=headteacher)
            dataList.append(d)
        return json.dumps(dataList)
    cno = request.args.get("cno","")
    level = request.args.get("level","")

    if cno !="":
        sql += " and t_class.cno="
        sql += str(cno)
    if level != "":
        sql += " and t_class.level="
        sql += str(level)
    print(sql)
    data = mysql.select(sql)

    for tp in data:
        d = {}
        id = tp[0]
        sname = tp[1]
        sno = tp[2]
        sex = tp[3]
        classid = tp[4]
        level = tp[5]
        cno = tp[6]
        headteacher = tp[7]
        d.update(id=id)
        d.update(sname=sname)
        d.update(sno=sno)
        d.update(sex=sex)
        d.update(classid=classid)
        d.update(level=level)
        d.update(cno=cno)
        d.update(headteacher=headteacher)
        dataList.append(d)
    return json.dumps(dataList)
@student_bp.route("/delete/",methods = ["GET"])
def delete_student():
    """
    删除账号
    :return:
    {
        "id":1
    }
    """
    id = request.args.get("id")
    sql = "delete from t_student where id=%s"%(id)
    res = mysql.insert(sql)
    print(res)
    if res["result"] is True:
        return {
            "desc":"删除成功!"
        }
@student_bp.route("/create/",methods = ["POST"])
def add_student():
    """
    添加
    {
        "sname":"张三",
        "sno":"20210101"
        "sex":"女"
        "classid":"2"
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    sname = data.get("sname","")
    sno = data.get("sno","")
    sex = data.get("sex","")
    classid = data.get("classid","")
    if sname == "" or sno =="" or sex == "" or classid =="":
        return {
            "desc":"所有字段均不可为空!请重新编辑!"
        }
    sql= 'select * from t_student where sno = "%s"'%(sno)
    print(sql)
    res = mysql.select(sql)
    if len(res) >0:
        return {
            "desc":"此学号已被录入!"
        }
    else:
        sql = 'insert into t_student (sname,sno,sex,classid) values("%s","%s","%s","%s")'%(sname,sno,sex,classid)
        res = mysql.insert(sql)
        return res

