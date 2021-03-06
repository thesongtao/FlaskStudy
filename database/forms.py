#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-18 14:22
# @Author  : 君去不知何时归
# @Site    : 
# @File    : forms.py
# @Desc:
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField,SubmitField
class NewNoteForm(FlaskForm):
    body = TextAreaField('Body',validators=[DataRequired()])
    submit=SubmitField('Save')
class EditForm(FlaskForm):
    body = TextAreaField('Body',validators=[DataRequired()])
    submit=SubmitField('Update')
class DeleteForm(FlaskForm):
    submit = SubmitField('删除')