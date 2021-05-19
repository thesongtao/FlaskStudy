#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 18:49
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : mtspider.py
# @Desc: 大致描述下此文件的内容吧。。。
# 声明:本作者所有源代码只可以用作技术学习,不可用做其他非法用途。
import requests
import json
from urllib.parse import urlencode,quote
params = {
     'cityName': '',
     'cateId': '0',
     'areaId': '0',
     # 'userId': '115874893',
     'uuid': '272860a72e174511b2b9.1620552397.1.0.0',
     'platform': '1',
     'partner': '126',
     'riskLevel': '1',
     'optimusCode': '10',
     'cityName':'四平',
     'page':"2"
}
#请求头
headers = {
    "Cookie": "lsu=; _lxsdk_cuid=1790e9c33b9c8-0e54c2194a684b-5771031-1fa400-1790e9c33b9c8; _hc.v=2bdb5755-31b9-b538-14f8-5252c6a0e729.1619784121; _lxsdk=1790e9c33b9c8-0e54c2194a684b-5771031-1fa400-1790e9c33b9c8; client-id=eff48d8b-cc65-4b27-aebf-29cfba92f173; uuid=272860a72e174511b2b9.1620552397.1.0.0; mtcdn=K; u=115874893; n=%E5%90%9B%E5%8E%BB%E4%B8%8D%E7%9F%A5%E4%BD%95%E6%97%B6%E5%BD%92; lt=4oxtkuq5qicgrvAx8HUdXjZM3VIAAAAAaw0AAPZpRLvXtI_x5kKmtip-htS_rvD__jWI0mu_oITO3EGVacUIofXuHOsKpiut12j0UA; mt_c_token=4oxtkuq5qicgrvAx8HUdXjZM3VIAAAAAaw0AAPZpRLvXtI_x5kKmtip-htS_rvD__jWI0mu_oITO3EGVacUIofXuHOsKpiut12j0UA; token=4oxtkuq5qicgrvAx8HUdXjZM3VIAAAAAaw0AAPZpRLvXtI_x5kKmtip-htS_rvD__jWI0mu_oITO3EGVacUIofXuHOsKpiut12j0UA; token2=4oxtkuq5qicgrvAx8HUdXjZM3VIAAAAAaw0AAPZpRLvXtI_x5kKmtip-htS_rvD__jWI0mu_oITO3EGVacUIofXuHOsKpiut12j0UA; unc=%E5%90%9B%E5%8E%BB%E4%B8%8D%E7%9F%A5%E4%BD%95%E6%97%B6%E5%BD%92; ci=1; rvct=1%",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
}
url_param = "https://sp.meituan.com/meishi/api/poi/getPoiList?" + urlencode(params)
url = "http://8.140.105.168:5000/mt/gettoken/?token=MTYyMDY0Mzc3MS41MDE4MDM5OmRiNGI3NTIwMThlOTdiZDY3MjA5NmQ2ZmM5NTkzZjM3ODRmNTdmNjk=&url="+url_param
print(url)
res = requests.get(url)
jstr = json.loads(res.text)
_token = jstr["_token"]
url_param +="&_token="
url_param +=_token
res = requests.get(url_param,headers=headers)
print(res.text)