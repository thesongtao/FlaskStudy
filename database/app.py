#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-17 21:10
# @Author  : 君去不知何时归
# @Site    : 
# @File    : app.py
# @Desc:
from flask import Flask,request,flash,redirect,url_for,render_template,abort
import click
from flask_sqlalchemy import SQLAlchemy
import os
from forms import NewNoteForm,EditForm,DeleteForm
import sys
import time
from flask_migrate import Migrate
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETKEY STRING"

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

#数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",prefix + os.path.join(app.root_path,"data.db"))
# 动态追踪修改设置，
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
@app.cli.command()
@click.option("--drop",is_flag=True,help='Create after drop.')
def initdb(drop):
    """
    自定义flask命令:初始化数据库
    :return:
    """
    if drop:
        click.confirm("确认清空数据库表,并删除么?",abort=True)
        db.drop_all()
        click.echo("已清空并删除表!")
    db.create_all()
    click.echo("数据库表已经重新创建!")


class Draft(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    edit_time = db.Column(db.Integer,default=0)
@db.event.listens_for(Draft.body,"set",named=True)
def increment_edit_time(**kwargs):
    if kwargs["target"].edit_time is not None:
        kwargs["target"].edit_time +=1
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    comments = db.relationship("Comment",
                               back_populates="post",
                               cascade="all,delete-orphan"
                               )
class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    post = db.relationship("Post",back_populates="comments")
class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True)
    phone = db.Column(db.String(20))
    articles = db.relationship("Article")

class Article(db.Model):
    author_id = db.Column(db.Integer,db.ForeignKey('bp_author.id'))
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),index=True,nullable=False)
    body = db.Column(db.Text)

class Writer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True,unique=True)
    books = db.relationship("Book",back_populates="writer")
class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),index=True)
    writer_id = db.Column(db.Integer,db.ForeignKey("writer.id"))
    writer = db.relationship("Writer",back_populates="books")

class Singer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True)
    songs = db.relationship("Song",backref='singer')
class Song(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(40),unique=True,index=True)
    singer_id = db.Column(db.Integer,db.ForeignKey("singer.id"))

class Citizen(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),unique=True)
    city_id = db.Column(db.Integer,db.ForeignKey("city.id"))
    city = db.relationship("City")
class City(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),unique=True)
class Country(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60),unique=True)
    capital = db.relationship("Capital",uselist=False)
class Capital(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60),unique=True)
    country_id = db.Column(db.Integer,db.ForeignKey("country.id"))
    country = db.relationship("Country")

association_table=db.Table(
                    'association',
                    db.Column("student_id",db.Integer,db.ForeignKey('student.id')),
                    db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')),
)
class Student(db.Model):
      id = db.Column(db.Integer,primary_key=True)
      name = db.Column(db.String(30),unique=True)
      grade = db.Column(db.String(30))
      teachers = db.relationship("Teacher",secondary=association_table,back_populates="students")
class Teacher(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(30), unique=True)
      office = db.Column(db.String(20))
      students = db.relationship("Student",secondary=association_table,back_populates="teachers")
class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.TIMESTAMP)
@app.route("/new",methods=["GET","POST"])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit(): #如果是POST提交,并且表单验证通过
        body = form.body.data
        note = Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash("Your note is saved.")
        time.sleep(0.8)
        return redirect(url_for("index"))
    return render_template('new_note.html',form=form)

@app.route("/")
@app.route("/index")
def index():
    form = DeleteForm()
    notes = Note.query.all()
    return render_template("index.html",notes=notes,form=form)

@app.route("/editnote/<int:noteid>",methods=["GET","POST"])
def edit_note(noteid):
    form = EditForm()
    note = Note.query.get(noteid)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash("Your note is updated.")
        return redirect(url_for('index'))
    form.body.data = note.body
    return render_template("editnote.html",form=form)
@app.route("/deletenote/<int:noteid>",methods=["GET","POST"])
def delete_note(noteid):
    form = DeleteForm()
    if form.validate_on_submit():
        note = Note.query.get(noteid)
        db.session.delete(note)
        db.session.commit()
        flash("your note is deleted.")
        return redirect(url_for("index"))
    else:
        abort(404)
    return redirect(url_for('index'))


@app.shell_context_processor
def make_shell_context():
    """
    shell上下文处理函数
    :return:
    """
    return dict(db=db,
                Note=Note,
                Author=Author,
                Article=Article,
                Writer=Writer,
                Book=Book,
                Post=Post,
                Comment=Comment,
                Draft=Draft,
                )
