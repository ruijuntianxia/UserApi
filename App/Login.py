#Login.py
# coding:utf-8
#__file__获取当前程序的相对路径
import os,sys
#print(__file__)
# os.path.abspath(__file__) 获取当前程序的绝对路径
print(os.path.abspath(__file__))
# E:\my python study\day4\Atm\bin\atm.py
Path=os.path.abspath(__file__)
# print(os.path.dirname(Path))获取当前程序的父目录的绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(Path))
print(BASE_DIR)
# E:\my python study\day4\Atm
#将BASE_DIR添加到系统环境变量中
sys.path.append(BASE_DIR)

from Apis import LoginCheck 

# flask 模块
import json
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import Request
from flask import request
from flask_cors import CORS
import redis




app = Flask(__name__)

CORS(app, resources=r'/*')
@app.route('/login/', methods=['GET', 'POST'])
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application():

    #post数据
    filed=request.data
    #IP
    Clientaddr=request.remote_addr
    #转码，将字节转换为字串
    filed=filed.decode()
    #处理转换为json
    filed=json.loads(filed) 

    r = redis.Redis(host='127.0.0.1', port=6379,db=2,password='zh123')
    retufile=LoginCheck.postLogin()
    #返回值

    return retufile  


@app.route('/logintk/', methods=['GET', 'POST'])
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def apptokenfile():
    filed=request.data
    #fileurl=request.environ
    #print(fileurl)
    filed=filed.decode()
    filed=json.loads(filed) 
    retufile=''
    return retufile 

    


if __name__ == "__main__":
    

    app.run(host="0.0.0.0",port=8009,debug=True)
    #app.run(host="localhost",port=8009)
    #app.run(host="172.18.218.223",port=8009)