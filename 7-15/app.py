from flask import Flask, render_template, request
from noe_spider import func
from pymongo import MongoClient
from selenium import webdriver

app = Flask(__name__)

app.debug = True

client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["thc"]

def GetInfo(user_id, passwd):
    Info = col.find({"学号":user_id})
    if Info.count() == 1:
        return Info[0]
        if Info[0]["passwd"] == passwd:
            return Info[0]
        else:
            return {}
    elif Info.count() == 0:
        Info = func(user_id,passwd)
        col.insert(Info)
        return Info


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