#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:14
# @Author  : 君去不知何时归
# @Site    : 
# @File    : forms.py
# @Desc:
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length
class HelloForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),Length(1,20)])
    body = TextAreaField("Message",validators=[DataRequired(),Length(1,200)])
    submmit = SubmitField()
