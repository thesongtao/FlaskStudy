#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 18:17
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : class.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Blueprint,request,current_app,send_file
from DBPool import MySQL
import json
import os
mysql = MySQL()
exem_bp = Blueprint("exem",__name__)

@exem_bp.route("/create/",methods = ["GET"])
def create_exem():
    """
    创建一次考试
    """
    #考试名称
    name = request.args.get("name","")
    #开始时间
    start_time = request.args.get("start_time","")
    #结束时间
    end_time = request.args.get("end_time","")
    if name == "" or start_time == "" or end_time =="":
        return {
            "desc":"所有输入均不允许为空!"
        }
    sql = 'insert into t_exam (name,start_time,end_time) values("%s","%s","%s")'%(name,start_time,end_time)
    print(sql)
    res = mysql.insert(sql)
    return res

@exem_bp.route("/delete/",methods = ["GET"])
def delete_exem():
    """
    删除考试记录主体
    :return:
    """
    exem_id = request.args.get("exam_id")
    #删除t_exam表数据
    sql = "delete from t_exam where exam_id=%s"%(exem_id)
    res = mysql.insert(sql)
    return res
@exem_bp.route("/select/",methods = ["GET"])
def select_exam():
    """
    查询所有考试主体
    :return:
    """
    sql = "select * from t_exam order by exam_id desc"
    res = mysql.select(sql)
    dataList = []
    for tp in res:
        data = {
            "exam_id": "",
            "name": "",
            "start_time":"",
            "end_time":""
        }
        id = tp[0]
        name = tp[1]
        start_time = tp[2]
        end_time = tp[3]
        data["exam_id"] = id
        data["name"] = name
        data["start_time"] = start_time
        data["end_time"] = end_time
        dataList.append(data)
    return json.dumps(dataList)
@exem_bp.route("/create/examsubject",methods = ["GET"])
def create_exam_subject():
    """
    添加考试科目
    :return:
    """
    examid = request.args.get("exam_id")
    subject_id = request.args.get("subject_id")
    question_file_path = request.args.get("question_file_path")
    answer_file_path = request.args.get("answer_file_path")
    sql = 'insert into t_exam_detail (exam_id,subject_id,question_file_path,answer_file_path) values("%s","%s","%s","%s")'%(examid,subject_id,question_file_path,answer_file_path)
    print(sql)
    res = mysql.insert(sql)
    if "Duplicate" in str(res):
        return {
            "desc":"请勿重复添加考试科目!"
        }
    return res
@exem_bp.route("/delete/examsubject",methods = ["GET"])
def delete_exam_subject():
    """
    删除考试对应的科目
    :return:
    """
    exam_detail_id = request.args.get("exam_detail_id")
    sql = "delete from t_exam_detail where exam_detail_id=%s"%(exam_detail_id)
    res = mysql.insert(sql)
    return res
@exem_bp.route("/select/examsubject",methods = ["GET"])
def select_exam_subjects():
    """
    查询考试下所有科目
    :return:
    """
    exam_id = request.args.get("exam_id")
    sql = "select d.*,s.name as subject_name from t_exam_detail d,t_subject s where d.subject_id=s.id and exam_id=%s"%(exam_id)
    res = mysql.select(sql)
    dataList = []
    for tp in res:
        data = {
            "exam_detail_id": "",
            "exam_id": "",
            "subject_id":"",
            "question_file_path": "",
            "answer_file_path": "",
            "is_upload_library":"",
            "subject_name":""
        }
        exam_detail_id = tp[0]
        exam_id = tp[1]
        subject_id = tp[2]
        question_file_path = tp[3]
        answer_file_path = tp[4]
        is_upload_library = tp[5]
        subject_name = tp[6]
        data["exam_detail_id"] = exam_detail_id
        data["exam_id"] = exam_id
        data["subject_id"] = subject_id
        data["question_file_path"] = question_file_path
        data["answer_file_path"] = answer_file_path
        data["is_upload_library"] = is_upload_library
        data["subject_name"] = subject_name
        dataList.append(data)
    return json.dumps(dataList)

@exem_bp.route("/create/gradereport",methods = ["GET"])
def create_exam_class_grade_report():
    """
    添加班级考试成绩单
    :return:
    """
    exam_id = request.args.get("exam_id")
    exam_detail_id = request.args.get("exam_detail_id")
    class_id = request.args.get("class_id")
    grade_file_path = request.args.get("grade_file_path")
    sql = 'insert into t_exam_class_grade_report (exam_id,exam_detail_id,class_id,grade_file_path) values("%s","%s","%s","%s")'%(exam_id,exam_detail_id,class_id,grade_file_path)
    res = mysql.insert(sql)
    if "Duplicate" in str(res):
        return {
            "desc":"成绩单不可重复上传!"
        }
    return res
@exem_bp.route("/delete/gradereport",methods = ["GET"])
def delete_exam_class_grade_report():
    """
    删除班级考试成绩单
    :return:
    """
    class_grade_report_id = request.args.get("class_grade_report_id")
    sql = 'delete from t_exam_class_grade_report where class_grade_report_id=%s'%(class_grade_report_id)
    res = mysql.insert(sql)
    return res
@exem_bp.route("/select/gradereport",methods = ["GET"])
def select_exam_class_grade_report():
    """
    查询某次考试下某个科目下的所有班级成绩
    :return:
    """
    exam_detail_id = request.args.get("exam_detail_id")
    sql ="""
        select c.level,c.cno,(select acco.realname from t_account acco where account=c.headteacher) as head_teacher_name ,grade.grade_file_path,grade.class_grade_report_id
		from t_exam_class_grade_report grade,t_class c
					where grade.class_id=c.id and grade.exam_detail_id=%s      
    """%(exam_detail_id)
    res = mysql.select(sql)
    dataList = []
    for tp in res:
        data = {
            "level": "",
            "cno": "",
            "header_teacher_name": "",
            "grade_file_path": "",
            "class_grade_report_id":"",
        }
        level = tp[0]
        cno = tp[1]
        header_teacher_name = tp[2]
        grade_file_path = tp[3]
        class_grade_report_id = tp[4]
        data["level"] = level
        data["cno"] = cno
        data["header_teacher_name"] = header_teacher_name
        data["grade_file_path"] = grade_file_path
        data["class_grade_report_id"] = class_grade_report_id
        dataList.append(data)
    return json.dumps(dataList)

@exem_bp.route("/file/upload",methods = ["POST"])
def file_upload():
    """
    文件上传
    :return:
    """

    #获取文件名
    filename = request.form.get("filename")
    #获取文件
    file = request.files["file"]
    stempic = request.form.get("stempic", "")
    if stempic == 1: #上传题干图片
        file_path = "/root/file/stem/{}.png".format(filename)
    else:
        file_path = "/root/file/" + filename
    #保存文件
    file.save(file_path)
    return {
        "desc":"文件上传成功!"
    }
@exem_bp.route("/file/download",methods = ["POST"])
def file_download():
    """
    文件下载
    :return:
    """
    data = request.get_data()
    data = json.loads(data)
    filename = data.get("filename","")
    answerpic = data.get("answerpic","")
    stempic = data.get("stempic","")
    if answerpic == "1":#下载答案
        file_path = "/root/file/pic/{}/{}.png".format(filename)
    elif stempic ==1:
        file_path = "/root/file/stem/{}.png".format(filename)
    else:
        file_path="/root/file/"+filename
    if os.path.isfile(file_path):
        return send_file(file_path,as_attachment=True)
    else:
        return {
            "desc":"下载文件不存在!"
        }
@exem_bp.route("/select/noupload",methods = ["GET"])
def select_no_upload():
    """
    查询所有没有上传到公共题库的考试试题记录
    :return:
    """
    sql = """
        select exam.exam_id,examdetail.exam_detail_id,exam.name,exam.start_time,subject.name,examdetail.question_file_path,examdetail.question_file_path
 			 
 	    from t_exam exam,t_exam_detail examdetail,t_subject subject
 		
				where examdetail.exam_id = exam.exam_id and examdetail.subject_id= subject.id and examdetail.is_upload_library=0 order by exam.start_time desc
    """
    res = mysql.select(sql)
    dataList = []
    for tp in res:
        data = {
            "exam_id":"",
            "exam_detail_id": "",
            "exam_name": "",
            "start_time": "",
            "subject_name": "",
            "question_file_path":"",
            "answer_file_path":""
        }
        exam_id = tp[0]
        exam_detail_id = tp[1]
        exam_name = tp[2]
        start_time = tp[3]
        subject_name = tp[4]
        question_file_path = tp[5]
        answer_file_path = tp[6]
        data["exam_id"] = exam_id
        data["exam_detail_id"] = exam_detail_id
        data["exam_name"] = exam_name
        data["start_time"] = start_time
        data["subject_name"] = subject_name
        data["question_file_path"] = question_file_path
        data["answer_file_path"] = answer_file_path
        dataList.append(data)
    return json.dumps(dataList)
