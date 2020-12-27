#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:14
# @Author  : 君去不知何时归
# @Site    : 
# @File    : views.py
# @Desc:
from flask import flash,redirect,render_template,url_for
from sayhello import app,db
from sayhello.models import Message
from sayhello.forms import HelloForm
@app.route("/",methods=["GET","POST"])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name
        body = form.body
        message = Message(body=body,name=name) #实例化模型类,创建记录
        db.message.add(message)#添加记录到数据库会话
        db.message.commit()#提交数据库会话
        flash("Your Message have been sent to the world!")
        return redirect(url_for("index")) #重定向index视图
    #加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html',form=form,messages=messages)