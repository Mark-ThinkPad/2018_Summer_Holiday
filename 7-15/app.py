from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route('/',methods=["POST","GET"])
def index():
    return render_template("base.html")

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