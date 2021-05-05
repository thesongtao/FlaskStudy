#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-05 15:53
# @Author  : 君去不知何时归
# @Site    : 
# @File    : main.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Flask,request
from bhjk.bhjk import bhjk_bp
from utiles.authtoken import *
#注册一个app
app = Flask(__name__)
#app上注册蓝图
app.register_blueprint(bhjk_bp,url_prefix="/bhjk")
#返回字典
resDict = {
    "desc":None,    #描述
    "code":None     #状态码
}

@app.before_request
def check_token():
    """
    检验token有效期
    """
    url = request.url
    if "gettoken" not in url:
        token = request.args.get("token","")
        if token is None or "":
            resDict["desc"] = "检查Token传入值!!!"
            return resDict

        cerres = certify_token(key,token)
        if cerres is False:
            resDict["desc"] = "TOKEN过期联系管理员!!!"
            return resDict
@app.route("/gettoken/",methods=["GET"])
def getToken():
    """
    注册token,
    pwd=thetao
    days:token有效期,传入1即为有效期一天,不传入token则默认值一天
    http://8.140.105.168:5000/gettoken/?pwd=thetao&days=1
    """
    pwd = request.args.get("pwd","")
    if pwd !="" and pwd == "thetao":
        days = int(request.args.get("days",1,))
        expire_times = 60*60*24*days
        token = generate_token(key,expire_times)
        return token
    resDict["desc"] = "token注册失败,检查管理员密码"
    return resDict
    generate_token(key)
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)