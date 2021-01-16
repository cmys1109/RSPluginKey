from flask import Flask,request,jsonify
import os,datetime,json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

sdir = os.path.dirname(__file__)

#无数据库版，直接用文件名+内容来做
def log(ip,tf):
    global sdir
    f = open(sdir + "\\logs","a")
    f.write("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] , " + ip + " , " + str(tf) + "\n")
    f.close()

def verify(ip,key):
    global sdir
    keydir = str(sdir + "\\keys\\" + ip)
    returnjson = {"state":False,"AD":"广告位招租！"}
    returntf = returnjson
    if os.path.isfile(keydir):
        with open(keydir,"r")as f:
            filekey = f.read()
        if key == filekey:
            returnjson["state"]=True
    log(ip,returntf)
    return jsonify(returnjson)

@app.route('/')
def hello_world():
    return '这是R&S开源项目 「插件授权」,开发者：cmys1109'

@app.route('/verify/<string:key>')
def verifymain(key):
    ip = str(request.remote_addr)
    return verify(ip,key)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"