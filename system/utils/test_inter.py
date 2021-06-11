#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 23:21
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : test_inter.py
# @Desc: 接口测试
import requests
headers = {'Content-Type': 'application/json;charset=UTF-8'}
# #登录
# data = {
#     "account":"root",
#     "pwd":"root"
# }
# url ="http://8.140.105.168:5002/user/login/"
# res = requests.post(url=url,json=data,headers=headers)
# print("登录:",res.text)

#创建用户
# data = {
#         "account":"教师2",
#         "pwd":"test",
#         "realname":"教师2",
#         "rid":"3"
#     }
# url ="http://127.0.0.1:5000/user/create/"
# res = requests.post(url=url,json=data,headers=headers)
# print("创建用户:",res.text)
#
# #删除用户
# data = {
#         "id":6
#     }
# url ="http://127.0.0.1:5000/user/delete/"
# res = requests.get(url=url,params=data)
# print("删除账号:",res.text)
#
#查询账户 type=1查询所有教师,type=0查询所有
# url ="http://127.0.0.1:5000/user/select/?type=0"
# res = requests.get(url=url)
# print("查询所有用户:",res.text)
#
#修改账号
# data = {
#         "id": "3",
#         "pwd": "sdfsdf",
#         "realname": "广坤",
#         "rid": "2"  # 1 root;2管理员;3老师
#     }
# url ="http://127.0.0.1:5002/user/update/"
# res = requests.post(url=url,json=data,headers=headers)
# print(res.text)
# #
# #----------------------班级管理-------------------------------------------------------
# #
# #添加班级
# url ="http://127.0.0.1:5000/class/create/"
# data = {
#         "level":"2021",
#         "cno":"3",
#         "headteacher":"秀儿"
# }
# res = requests.post(url=url,json=data,headers=headers)
# print("添加班级:",res.text)
# # 删除班级
# data = {
#         "id":1
#     }
# url ="http://127.0.0.1:5000/class/delete/"
# # res = requests.get(url=url,params=data)
# # print("删除班级:",res.text)
# #修改班级
# data = {
#         "id": "2",
#         "headteacher":"天秀儿"
#     }
# url ="http://127.0.0.1:5000/class/update/"
# res = requests.post(url=url,json=data,headers=headers)
# print(res.text)
#查询班级
# url ="http://127.0.0.1:5002/class/select/?level=2020&headteacher=%E6%95%99%E5%B8%881"
# res = requests.get(url=url)
# print("查询班级:",res.text)
#
# #
# #----------------------学生管理-------------------------------------------------------
# #
# #添加学生
# url ="http://127.0.0.1:5000/student/create/"
# data = {
#         "sname":"李四",
#         "sno":"20210101",
#         "sex":"女",
#         "classid":"2"
# }
# res = requests.post(url=url,json=data,headers=headers)
# print("添加学生:",res.text)
# #删除学生
# # data = {
# #         "id":2
# # }
# # url ="http://127.0.0.1:5000/student/delete/"
# # res = requests.get(url=url,params=data)
# # print("删除学生:",res.text)
#
# #修改学生
# data = {
#         "id": "3",
#         "classid":"2"
#     }
# url ="http://127.0.0.1:5000/student/update/"
# res = requests.post(url=url,json=data,headers=headers)
# print("修改学生信息:",res.text)
# #查询学生信息
# data ={
#     # "all":1,  #查询所有学生 传1,不查询所有学生,不用传
#     "level":2021, #年级 查询哪一级的学生
#     "cno":1  #查询班级
# }
# url ="http://8.140.105.168:5002/student/select/"
# res = requests.get(url=url,params=data,headers=headers)
# print("查询学生:",res.text)

#
#----------------------学科管理-------------------------------------------------------
#
# url ="http://127.0.0.1:5002/subject/select/"
# res = requests.get(url=url)
# print("查询学科:",res.text)
#
#----------------------考试管理-------------------------------------------------------
#
#创建考试
# url ="http://127.0.0.1:5002/exam/create/?name=月考&start_time=2021-06-07 08:00:00&end_time=2021-06-10 08:00:00"
# res = requests.get(url=url)
# print("创建考试:",res.text)
#删除考试
# url ="http://127.0.0.1:5002/exam/delete/?exam_id=2"
# res = requests.get(url=url)
# print("删除考试:",res.text)
#查询考试信息
# url ="http://127.0.0.1:5002/exam/select/"
# res = requests.get(url=url)
# print("查询考试:",res.text)
#创建具体考试科目
# url ="http://8.140.105.168:5002/exam/create/examsubject?exam_id=4&subject_id=6&question_file_path=/root/kaoshi.doc&answer_file_path=kaoshi_answer.doc"
# res = requests.get(url=url)
# print("创建具体考试科目:",res.text)
#查询某次考试所有科目
# url ="http://8.140.105.168:5002/exam/select/examsubject?exam_id=6"
# res = requests.get(url=url)
# print("查询某次考试所有科目:",res.text)
#添加班级考试成绩单
# url ="http://127.0.0.1:5002/exam/create/gradereport?exam_id=4&exam_detail_id=4&class_id=5&grade_file_path=4_5_2020_3_grade.xml"
# res = requests.get(url=url)
# print("添加班级考试成绩单:",res.text)
#查询某次考试某个科目下的所有班级成绩报告
# url ="http://127.0.0.1:5002/exam/select/gradereport?exam_detail_id=33"
# res = requests.get(url=url)
# print("查询某个科目下所有班级成绩单:",res.text)

# 文件上传 (表单提交)Post
# url ="http://8.140.105.168:5002/exam/file/upload?"
# data = {
#     "filename":"wl_1234567891234__123456789123.png",
#     "stempic":1,
# }
# files = {"file":""}
# with open("C:\\Users\\18629\\Desktop\\test.png",mode='rb') as f:
#     file = f.read()
#     files["file"] = file
# res = requests.post(url,data=data,files=files)
# print(res.text)
#文件下载
# url ="http://8.140.105.168:5002/exam/file/download?"
# data = {
#     "filename":"wl_1234567891234__123456789123.png",
#     "stempic":1
# }
# res = requests.post(url,json=data)
# with open("wl_1234567891234__123456789123.png",mode='wb') as f:
#     f.write(res.content)

#查询还没有上传到公共试题的考试记录
# url ="http://127.0.0.1:5002/exam/select/noupload"
# res = requests.get(url)
# print(res.text)

#查询知识点图谱
# url ="http://127.0.0.1:5002/knowledge/getnode?&parentid=0&subjectid=4"
# res = requests.get(url)
# print(res.text)
#查询题库 POST JSON
# url ="http://127.0.0.1:5002/question/select/"
# data = {
#     "libtype":1, #1公共题库, 2推荐题库
#     "keyword":"牛顿第二定律的同向性||平衡状态的定义及条件" #知识点进行点选添加到搜索条件,然后点击确定搜索
# }
# res = requests.post(url=url,json=data,headers=headers)
# print(res.text)
#删除题库试题
# url ="http://8.140.105.168:5002/question/delete/?libtype=2&id=16706"
# res = requests.get(url)
# print(res.text)
#添加试题到题库
# url ="http://127.0.0.1:5002/question/add/"
# data = {
#     "libtype":"1",
#     "qtype":"测试题",
#     "difficulty":"0.85",
#     "nums":"0", #创建传0就行
#     "qno":"", #wl_时间戳 名命题号
#     "stem":"厉害", #保存html样式
#     "source":"", #梨树一中
#     "points":"", #牛顿第一定律 第三定律    #此项需要从知识图谱中进行添加
#     "answer":"",#保存文本的html样式 ,新上传的题没有图片答案。
#     "exam_detail_id":0, #是否为考试题(如果为考试题,选择哪场考试的哪个科目把id传过来,非考试为空。)
#     "subject_id":"4"
# }
# res = requests.post(url=url,json=data,headers=headers)
# print(res.text)

#试题更新
# url ="http://127.0.0.1:5002/question/update/"
# data = {
#     "libtype":"1",
#     "qtype":"测试题",
#     "difficulty":"0.85",
#     "nums":"1", #创建传0就行
#     "qno":"1623216962626", #wl_时间戳 名命题号
#     "stem":"&amp;lt;p&amp;gt;真实牛逼了士大夫&amp;nbsp;我去了。想想都刺激&amp;lt;/p&amp;gt;", #保存html样式
#     "source":"", #梨树一中
#     "points":"", #牛顿第一定律 第三定律    #此项需要从知识图谱中进行添加
#     "answer":"",#保存文本的html样式 ,新上传的题没有图片答案。
#     "exam_detail_id":0, #是否为考试题(如果为考试题,选择哪场考试的哪个科目把id传过来,非考试为空。)
#     "id":"16708"
# }
# res = requests.post(url=url,json=data,headers=headers)
# print("试题更新:",res.text)
#试题匹配
# url ="http://127.0.0.1:5002/question/matching/"
# data = {
#     "libtype":1,
#     "subject_id":"4",
#     "text":"梨树一中"
# }
# res = requests.post(url=url,json=data)
# print(res.text)

#查询试题 题型列表
url = "http://127.0.0.1:5002/question/qtype/"
res = requests.get(url)
print(res.text)