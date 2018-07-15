from flask import Flask, render_template, request, jsonify
from noe_spider import func
from pymongo import MongoClient
from selenium import webdriver
import json
from bson import json_util

app = Flask(__name__)

app.debug = True

client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["thc"]

def GetInfo(user_id, passwd):
    info = col.find({"user_id":user_id})
    if info.count() == 1:
        if info[0]["passwd"] == passwd:
            return json.dumps(info[0],default=json_util.default)
        else:
            return False
    elif info.count() == 0:
        info = func(user_id, passwd)
        col.insert(info)
        return info

@app.route('/',methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route('/info',methods=["POST","GET"])
def showInfos():
    if request.method == "GET":
        content = "兄弟,你的操作有问题啊"
        return render_template("error.html",content=content)
    elif request.method == "POST":
        user_id = request.form["username"]
        passwd = request.form["password"]
        #print(user_id)
        #print(passwd)
        Infos = GetInfo(user_id, passwd)
        return render_template("info.html", content=Infos)
    return render_template("index.html")

@app.route("/api/info",methods=["POST", "GET"])
def api_info():
    if request.method == "GET":
        content = "你没有填数据吧"
        return str({"message":content})
    elif request.method == "POST":
        user_id = request.form["username"]
        password = request.form["password"]
        infos = GetInfo(user_id,password)
        res = jsonify(infos)
        res.headers['Access-Control-Allow-Origin'] = '*'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Methods'] = 'POST，GET,OPTIONS'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'.encode("utf-8").decode("latin1")
        return res


@app.errorhandler(405)
def error(e):
    content = "找不到吧哈哈哈-405"
    return render_template("error.html",content=content)

@app.errorhandler(404)
def error(e):
    content = "找不到略略略-404"
    return render_template("error.html",content=content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)