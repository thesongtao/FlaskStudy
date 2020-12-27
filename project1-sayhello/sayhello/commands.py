#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-21 18:15
# @Author  : 君去不知何时归
# @Site    : 
# @File    : commands.py
# @Desc:
from app import db,app
import click
@app.cli.command()
@click.option("--drop",is_flag=True,help="Create after drop")
def initdb(drop):
    if drop:
        click.confirm("确认清空数据表么?",abort=True)
        db.drop_all()
        click.echo("已清空数据表!")
    db.create_all()
    click.echo("数据库初始化成功!")