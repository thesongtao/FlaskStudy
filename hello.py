#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-10 10:59
# @Author  : 君去不知何时归
# @Site    : 
# @File    : hello.py
# @Desc:
from flask import Flask,request,redirect,jsonify,make_response,session,g
import json
import os
from flask import url_for
import click
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/greet/<name>")
def greet(name):
    print(request.args.get("age"))
    return "Hello  %s !" %name
@app.route("/test")
def test():
    return redirect(url_for("greet",**{"name":"song","age":1}))
@app.route('/login')
def login():
    session["logged_in"] = True
    return redirect(url_for('hello'))
@app.route("/")
@app.route("/hello")
def hello():
    name = request.cookies.get("name")
    age = request.args.get("age")
    print("age:",age)
    response = "<h1>Hello,%s!</h1>"
    if name is None:
        name = request.cookies.get("name","Human")
        response=response%(name)
    if 'logged_in' in session: #登录状态
        response += "[Authenticated]"
    else:
        response += "[Not Authenticated]"
    return response

@app.route("/set/<name>")
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name',name)
    return response

@app.before_request
def get_name():
    g.host = request.remote_addr

@app.route("/foo")
def foo():
    print(request.host_url)
    return "<h1>Foo page </h1><a href='%s'> Do something</a>" %(url_for('do_something',next=request.full_path))

@app.route("/bar")
def bar():
    return "<h1>Bar page </h1><a href='%s'> Do something</a>" % (url_for('do_something'))
@app.route("/do_something")
def do_something():
    import time
    time.sleep(3)
    return redirect(request.referrer)
@app.route("/xss")
def xss():
    name = request.args.get("name")
    response = '<h1>Hello, %s !</h1>' %(name)
    return response
if __name__ == '__main__':
    param = "'or 1=1 --"
    sql =  "select * from bhjk_spider where gname ='%s';"%(param)
    print(sql)