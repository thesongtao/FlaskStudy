#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-06-11 12:58
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : deal_data.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from DBPool import MySQL
import time
mysql = MySQL()

sql = "select id from t_question_tuijian"
res = mysql.select(sql)
print(len(res))
n = 1
for tp in res:
    timestamp = int(time.time()*1000)
    print(timestamp)
    id = tp[0]
    sql = "update t_question_tuijian set qno=%s where id=%s"%(timestamp,id)
    res = mysql.insert(sql)
    print("处理第{}条数据".format(n))
    n+=1
    print(res)
