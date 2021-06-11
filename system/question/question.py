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
import time
import html
import jieba.analyse as analyse
import jieba
mysql = MySQL()
question_bp = Blueprint("question",__name__)

@question_bp.route("/select/",methods = ["POST"])
def select_question():
    """
    题目查询
    """
    data = request.get_data()
    data = json.loads(data)
    libtype = data.get("libtype","")#选择题库 1:公共题库  2:推荐题库
    if str(libtype) == "":
        return {"desc":"请选择查询的题库!"}
    keywords = data.get("keyword","")#搜索内容为知识点搜索,多个知识点以||分割
    subject_id = data.get("subject_id","")
    if keywords == "":
        return {"desc":"选择知识点进行搜索!"}
    if str(libtype)=="1":
        table = "t_question_open"
    else:
        table = "t_question_tuijian"
    finalsql = ""
    for keyword in keywords.split("||"):
        sql = 'select * from {} where points like"%{}%" and subject_id={} '.format(table,keyword,subject_id)
        finalsql += sql +"\n union"
    finalsql = finalsql.split("union")[0]
    # print(finalsql)
    res = mysql.select(finalsql)
    # print(res)
    dataList = []
    for tp in res:
        data = {
            "id":"",
            "qtype":"",
            "difficulty":"",
            "nums":"",
            "update_time":"",
            "qno":"",
            "stem":"",
            "source":"",
            "points":"",
            "answer":"",
            "weburl":"",
            "isdownload":"",
            "exam_detail_id":""
        }
        id = tp[0]
        qtype = tp[1]
        difficulty = tp[2]
        nums = tp[3]
        update_time = tp[4]
        qno = tp[5]
        stem = tp[6]
        source = tp[7]
        points = tp[8]
        answer = tp[9]
        weburl = tp[10]
        isdownload = tp[11]
        exam_detail_id = tp[12]
        data["id"] = id
        data["qtype"] = qtype
        data["difficulty"] = difficulty
        data["nums"] = nums
        data["update_time"] = update_time
        data["qno"] = qno
        data["stem"] = stem
        data["source"] = source
        data["points"] = points
        data["answer"] = answer
        data["weburl"] = weburl
        data["isdownload"] = isdownload
        data["exam_detail_id"] = exam_detail_id
        dataList.append(data)
    return json.dumps(dataList)

@question_bp.route("/delete/",methods = ["GET"])
def delete_question():
    """
    删除试题
    :return:
    """
    libtype = request.args.get("libtype")#选择题库 1:公共题库  2:推荐题库
    if str(libtype)=="1":
        table = "t_question_open"
    else:
        table = "t_question_tuijian"
    id = request.args.get("id")#试题id
    sql = "delete from %s where id=%s"%(table,id)
    res = mysql.insert(sql)
    # print(res)
    return res

@question_bp.route("/add/",methods = ["POST"])
def add_question():
    """
    添加试题到题库
    :return:
    """

    data = request.get_data()
    jstr = json.loads(data)
    libtype = jstr.get("libtype")  # 选择题库 1:公共题库  2:推荐题库
    subject_id = jstr.get("subject_id")
    if str(libtype) == "1":
        table = "t_question_open"
    else:
        table = "t_question_tuijian"
    qtype = jstr.get("qtype","")
    difficulty = jstr.get("difficulty", "")
    nums = jstr.get("nums", "")
    update_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    qno = jstr.get("qno", "")
    stem = jstr.get("stem", "")
    stem = html.escape(stem)
    source = jstr.get("source", "")
    points = jstr.get("points", "")
    answer = jstr.get("answer", "")
    exam_detail_id = jstr.get("exam_detail_id","")
    sql = """
            insert into {} (qtype,difficulty,nums,update_time,qno,stem,source,points,answer,exam_detail_id,subject_id) 
                values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            
          """.format(table,qtype,difficulty,nums,update_time,qno,stem,source,points,answer,exam_detail_id,subject_id)
    # print(sql)
    res = mysql.insert(sql)
    # print(res)
    return res


@question_bp.route("/update/", methods=["POST"])
def update_question():
    """
    添加试题到题库
    :return:
    """

    data = request.get_data()
    jstr = json.loads(data)
    libtype = jstr.get("libtype")  # 选择题库 1:公共题库  2:推荐题库
    if str(libtype) == "1":
        table = "t_question_open"
    else:
        table = "t_question_tuijian"
    id = jstr.get("id","")
    qtype = jstr.get("qtype", "")
    difficulty = jstr.get("difficulty", "")
    nums = jstr.get("nums", "")
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    qno = jstr.get("qno", "")
    stem = jstr.get("stem", "")
    stem = html.escape(stem)
    source = jstr.get("source", "")
    points = jstr.get("points", "")
    answer = jstr.get("answer", "")
    exam_detail_id = jstr.get("exam_detail_id", "")
    sql = """
            update {} set qtype="{}",difficulty="{}",nums="{}",update_time="{}",qno="{}",
                          stem="{}",source="{}",points="{}",answer="{}",exam_detail_id="{}" 
                where id = "{}"
          """.format(table,qtype, difficulty, nums, update_time, qno, stem, source, points, answer, exam_detail_id,id)
    # print(sql)
    res = mysql.insert(sql)
    # print(res)
    return res
@question_bp.route("/matching/", methods=["POST"])
def matching_questions():
    """
    匹配试题
    :return:
    """
    data = request.get_data()
    jstr = json.loads(data)
    libtype = jstr.get("libtype","")  # 选择题库 1:公共题库  2:推荐题库
    if str(libtype) == "1":
        table = "t_question_open"
    else:
        table = "t_question_tuijian"
    subject_id = jstr.get("subject_id")
    text = jstr.get("text","")#题干文本,不包含html标签
    text = str(text)
    if text == "":
        return "[]"
    # keywords = jieba.analyse.extract_tags(text, topK=8, withWeight=False, allowPOS=(), withFlag=False)
    keywords = text.split("，")
    sql = 'select * from {} where subject_id={} and stem like "%{}" '
    s = ""
    for keyword in keywords:
        s+= keyword
        s+="%"
    sql = sql.format(table,subject_id,s)
    # print(sql)
    res = mysql.select(sql)
    dataList = []
    for tp in res:
        data = {
            "id": "",
            "qtype": "",
            "difficulty": "",
            "nums": "",
            "update_time": "",
            "qno": "",
            "stem": "",
            "source": "",
            "points": "",
            "answer": "",
            "weburl": "",
            "isdownload": "",
            "exam_detail_id": ""
        }
        id = tp[0]
        qtype = tp[1]
        difficulty = tp[2]
        nums = tp[3]
        update_time = tp[4]
        qno = tp[5]
        stem = tp[6]
        source = tp[7]
        points = tp[8]
        answer = tp[9]
        weburl = tp[10]
        isdownload = tp[11]
        exam_detail_id = tp[12]
        data["id"] = id
        data["qtype"] = qtype
        data["difficulty"] = difficulty
        data["nums"] = nums
        data["update_time"] = update_time
        data["qno"] = qno
        data["stem"] = stem
        data["source"] = source
        data["points"] = points
        data["answer"] = answer
        data["weburl"] = weburl
        data["isdownload"] = isdownload
        data["exam_detail_id"] = exam_detail_id
        dataList.append(data)
    return json.dumps(dataList)

@question_bp.route("/qtype/", methods=["GET"])
def select_qtype():
    """
    查询题型列表
    :return:
    """
    sql = "select typename from t_question_type"
    datas = mysql.select(sql)
    typenamelist = []
    for tp in datas:
        typenamelist.append(tp[0])
    return {
        "qtype_name_list":typenamelist
    }