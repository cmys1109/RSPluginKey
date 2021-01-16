import os,json,random
sdir = os.path.dirname(__file__)

# f = open(sdir+"\\str","r")
# fl = open(sdir+"\\str.txt","w")
# cont = f.read()
# json.dump(cont.split(" "),fl)

def makenewkey(ip):
    global sdir
    if not os.path.isfile(sdir + "\\keys\\" + ip):
        string = open(sdir + "\\str.txt","r")
        strs = json.load(string)
        x = 0
        key = ""
        while x <= 11:
            key += strs[random.randint(0,int(len(strs)-1))]
            x += 1
        f = open(sdir + "\\keys\\" + ip,"w")
        f.write(key)
        f.close()
        print("key:  "+key+"  ,ip:  "+cmd[1]+"  ,已经创建！")
    else:
        print("此IP已经绑定key！修改key请使用 'changekey [IP]'")

def changekey(ip,ckey):
    if ckey == "random":
        global sdir
        string = open(sdir + "\\str.txt","r")
        strs = json.load(string)
        x = 0
        key = ""
        while x <= 11:
            key += strs[random.randint(0,int(len(strs)-1))]
            x += 1
        f = open(sdir + "\\keys\\" + ip,"w")
        f.write(key)
        f.close()
        print("key:  "+key+"  ,ip:  "+cmd[1]+"  ,已经修改！")
    else:
        f = open(sdir + "\\keys\\" + ip,"w")
        f.write(ckey)
        f.close()

if __name__ == "__main__":
    print("后台key管理已经加载！欢迎使用！")
    while True:
        cmd = input("输入指令：").split(" ")
        if cmd[0] == "newkey" and len(cmd) == 2:
            makenewkey(cmd[1])
        elif cmd[0] == "q":
            print("正在结束！再见！")
            break
        elif cmd[0] == "changekey" and len(cmd) == 2 or 3:
            if len(cmd) == 2:
                changekey(cmd[1],"random")
            elif len(cmd) == 3:
                cont = input("确定要自定义key？ 自定义key为：" + cmd[2]+"  q退出，其他键继续！")
                if cont == "q":
                    pass
                else:
                    changekey(cmd[1],cmd[2])
                    print("key:  "+ cmd[2] +"  ,ip:  "+cmd[1]+"  ,已经修改！")
        else:
            print("未知指令！")
