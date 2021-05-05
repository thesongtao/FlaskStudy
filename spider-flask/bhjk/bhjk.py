#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-05 16:04
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : bhjk.py
# @Desc: 薄荷健康接口蓝图
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
from flask import Blueprint,request
import requests
bhjk_bp = Blueprint("bhjk",__name__)
headers = {
    "author-key":"4125b02c-81bf-4e22-97ea-ccfcdf205d30",
    "device-token":"6b873912-13c4-4109-9ed3-f43f89f6ef3e",
    "token":"MqW6rs3eyrAozszjMZMmmz7qhQp7Bd14"
}
#返回字典
resDict = {
    "desc":None,
    "code":None
}
@bhjk_bp.route("/search/",methods=["GET"])
def search():
    """
    食物搜索
    http://8.140.105.168:5000/bhjk/search/?keyword=猪肉&page=1&token=MTYxOTE0NTg4MS4wNTY4NjM6MGY0MjA2YmZlNWZiZWJlN2Q1OGNkYTViYmI1ZWIwMWIwNDNiNmI3Zg==
    """
    keywords = request.args.get("keyword")
    page = request.args.get("page")
    url = "https://food.boohee.com/fb/v1/search?app_version=7.7.8&phone_model=G011C&token=MqW6rs3eyrAozszjMZMmmz7qhQp7Bd14&app_device=Android&user_key=4125b02c-81bf-4e22-97ea-ccfcdf205d30&q={}&os_version=5.1.1&page_from=app_homepage&channel=tencent&page={}".format(keywords,page)
    res = requests.get(url,headers=headers)
    return res.text
@bhjk_bp.route("/detail/",methods=["GET"])
def food_detail():
    """
    食物详情
    http://8.140.105.168:5000/bhjk/detail/?code=zhurou_shou&token=MTYyMDMxMDcxMC40NDk3NDUyOmFlYzUyMjczMjRiOTcyYTM5MzhjMTMwYmQ5NmZlYTMyYTQwMzNjZjI=
    """
    code = request.args.get("code")
    url = "https://food.boohee.com/fb/v1/foods/{}".format(code)
    res = requests.get(url,headers=headers)
    return res.text
@bhjk_bp.route("/scan/",methods=["GET"])
def scan_food():
    """
    扫描食物,输入条形码code获取食物详情
    scode :条形码id
    http://8.140.105.168:5000/bhjk/scan/?scode=6922507012093&token=MTYyMDMxMDcxMC40NDk3NDUyOmFlYzUyMjczMjRiOTcyYTM5MzhjMTMwYmQ5NmZlYTMyYTQwMzNjZjI=
    """
    scode = request.args.get("scode")
    url = "https://food.boohee.com/fb/v1/foods/barcode?barcode={}".format(scode)
    res = requests.get(url,headers=headers)
    return res.text