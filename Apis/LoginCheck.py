#LoginCheck
# coding:utf-8
import json
import jwt
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import Request
from flask import request
from flask_cors import CORS
import binascii
import os
import pymysql
 



def postLogin(filed,clientaddr):  
    # 定义文件请求的类型和当前请求成功的code
    #start_response('200 OK', [('Content-Type', 'application/json')])
    
    # environ是当前请求的所有数据，包括Header和URL，body
    
    username=str(filed['Name']).upper()
    password=filed['Password']
    typefile=filed['Type']
    token=filed['token']

    # 打开数据库连接
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")
    
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    
    print ("Database version : %s " % data)
    
    # 关闭数据库连接
    db.close()
    dic ={"file":"","token":"","message":"false","resultcode":-4} # token 失效
    return dic
    