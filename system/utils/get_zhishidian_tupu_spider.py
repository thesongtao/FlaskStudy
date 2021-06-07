#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 15:42
# @Author  : 玛卡玛卡
# @Site    : 
# @File    : get_zhishidian_tupu_spider.py
# @Desc: 知识图谱采集入库
import requests
from DBPool import MySQL
from lxml import etree
mysql = MySQL()
url = "https://zujuan.xkw.com/gzwl/zsd41934/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Host": "zujuan.xkw.com"
}

def DiGui(html,parantID):
    #获取当前路径下的所有li节点
    li_list = html.xpath("./li[contains(@class,'tree-node')]")
    for li in li_list:
        #获取当前节点知识点名称
        nodename = li.xpath("./div/a/@title")[0]
        #获取当前知识点节点id->tree-id
        #将当前节点插入数据库
        tree_id = li.xpath("./@tree-id")[0]
        print("nodename:", nodename)
        print("tree_id:", tree_id)
        #遍历下一节点ul是否存在,存在则递归
        ul = li.xpath("./ul[@class='tree-ul']")
        if len(ul) >0: #如果下一节点存在则递归遍历
            is_have_childe =1 #当前节点有子节点则为1
            sql = 'insert into t_knowledge_points_tree (tree_id,name,parent_id,is_have_childe,subject_id) values (%s,"%s",%s,%s,%s)' % (tree_id, nodename, parantID, is_have_childe,4)
            res = mysql.insert(sql)
            print(res)
            ul = ul[0]
            DiGui(ul,tree_id)
        else:
            is_have_childe = 0 #没有子节点
            sql = 'insert into t_knowledge_points_tree (tree_id,name,parent_id,is_have_childe,subject_id) values (%s,"%s",%s,%s,%s)' % (
            tree_id, nodename, parantID, is_have_childe, 4)
            res = mysql.insert(sql)
            print(res)
    pass
if __name__ == '__main__':
    res = requests.get("https://zujuan.xkw.com/gzwl/zsd41934/",headers=headers)
    html = etree.HTML(res.text)
    ul = html.xpath("//ul[@class='tree-ul tree-top-ul']")[0]
    DiGui(ul,0)

