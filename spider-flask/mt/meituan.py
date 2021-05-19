#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 18:17
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : meituan.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Blueprint,request
from urllib.parse import quote
import execjs
meituan_bp = Blueprint("meituan",__name__)
js_exec = None
with open("./js/_token_20210509.js", mode='r') as f:
    js = f.read()
    js_exec = execjs.compile(js)
@meituan_bp.route("/gettoken/",methods = ["GET"])
def get_token():
    global js_exec
    url = request.args.get("url",None)
    if url is None:
        return {
            "desc":"检查传入参数!!!",
            "code":""
        }
    _token = js_exec.call("get_token", url)
    return {
        "_token":quote(_token),
        "desc":"成功计算_token"
    }