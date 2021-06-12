#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-05 15:53
# @Author  : 君去不知何时归
# @Site    : 
# @File    : main.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Flask,current_app
from user.user import user_bp
from tclass.tclass import class_bp
from student.student import student_bp
from subject.subject import subject_bp
from exem.exem import exem_bp
from knowledge.knowledge import knowledge_bp
from question.question import question_bp
from intelligence.intelligence import intelligence_bp
import logging
#注册一个app
app = Flask(__name__)
##app上注册蓝图
#注册账号管理蓝图
app.register_blueprint(user_bp,url_prefix="/user")
#注册班级管理蓝图
app.register_blueprint(class_bp,url_prefix="/class")
#注册学生管理蓝图
app.register_blueprint(student_bp,url_prefix="/student")
#注册学科管理蓝图
app.register_blueprint(subject_bp,url_prefix="/subject")
#注册考试管理蓝图
app.register_blueprint(exem_bp,url_prefix="/exam")
#知识点图谱管理蓝图
app.register_blueprint(knowledge_bp,url_prefix="/knowledge")
#注册智能推荐管理蓝图
app.register_blueprint(intelligence_bp,url_prefix="/intelligence")
# 在创建 app 之前将 log 级别重置为debug，让其线上 info 日志级别
logging.basicConfig(level=logging.INFO)
#题库管理
app.register_blueprint(question_bp,url_prefix="/question")
app.config['MAX_CONTENT_PATH'] = 1024*1024
#返回字典
if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logging.basicConfig(level=gunicorn_logger.level, handlers=gunicorn_logger.handlers)
    app.logger.handlers = gunicorn_logger.handlers
    app.run(debug=True, host='0.0.0.0', port=5002)
if __name__ != '__main__':
    # 如果不是直接运行，则将日志输出到 gunicorn 中
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logging.basicConfig(level=gunicorn_logger.level, handlers=gunicorn_logger.handlers)
    app.logger.handlers = gunicorn_logger.handlers