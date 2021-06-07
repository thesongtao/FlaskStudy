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
user_bp = Blueprint("user",__name__)

@user_bp.route("/update/",methods = ["POST"])
def update_account():
    """
    修改账号
    {
        "id":"3"
        "account":"管理员1",
        "pwd":"test"
        "realname":"管理员1"
        "rid":"2"   #1 root;2管理员;3老师
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    pwd = data.get("pwd","")
    realname = data.get("realname","")
    id = data.get("id")
    rid = data.get("rid","")
    sql = 'update t_account set pwd="%s",realname="%s",rid="%s" where id="%s"'%(pwd,realname,rid,id)
    print(sql)
    res = mysql.insert(sql)
    return res

@user_bp.route("/select/",methods = ["GET"])
def select_all():
    """
    查询账号如果 type=1 查询所有教师账号;type=0查询所有账号(管理员+老师)
    :return:
    """
    t = request.args.get("type")
    if str(t) == "1":
        sql = "select * from t_account where rid= 3 and rid!=1"
    else:
        sql = "select * from t_account where rid!=1"
    res = mysql.select(sql)

    userList = []
    for tp in res:
        id = tp[0]
        account = tp[1]
        realname = tp[3]
        rid = tp[4]
        userList.append({
            "id":id,
            "account":account,
            "realname":realname,
            "rid":rid
        })
    return json.dumps(userList)
@user_bp.route("/delete/",methods = ["GET"])
def delete_account():
    """
    删除账号
    :return:
    {
        "id":2
    }
    """
    id = request.args.get("id")
    sql = "delete from t_account where id=%s"%(id)
    res = mysql.insert(sql)
    print(res)
    if res["result"] is True:
        return {
            "desc":"删除成功!"
        }
@user_bp.route("/create/",methods = ["POST"])
def create_account():
    """
    创建账号
    {
        "account":"管理员1",
        "pwd":"test"
        "realname":"管理员1"
        "rid":"2"   #1 root;2管理员;3老师
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    account = data.get("account","")
    pwd = data.get("pwd", "")
    realname = data.get("realname", "")
    rid = data.get("rid", "")
    if account == "" or pwd == "" or realname == "" or rid == "":
        return {
            "desc":"检查账户名,密码,姓名,角色,是否有空项!"
        }
    sql= 'select * from t_account where account = "%s"'%(account)
    print(sql)
    res = mysql.select(sql)
    if len(res) >0:
        return {
            "desc":"账号名存在,请修改!"
        }
    else:
        sql = 'insert into t_account (account,pwd,realname,rid) values("%s","%s","%s","%s")'%(account,pwd,realname,rid)
        res = mysql.insert(sql)
        return res
@user_bp.route("/login/",methods = ["POST"])
def login():
    """
    登录
    入参 {
        "account":"root",
        "pwd":"root"
    }
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    account = data.get("account","")
    pwd = data.get("pwd", "")
    sql = 'select account,rid from t_account where account="%s" and pwd= "%s"'%(account,pwd)
    res = mysql.select(sql)
    if len(res) >0:
        return {
            "account":res[0][0],
            "rid":res[0][1]
        }
    else:
        return {
            "account":"",
            "rid":""
        }

