# RSPluginKey
D&amp;M RS开源项目-RSPluginKey，让每位开发者给自己的插件装上授权！
## 前端cpp（在写）

## 后端python flask（初代完工）
### 运行环境配置
 推荐python3.6以上  
 安装flask（pip install flask)  
 安装requests（pip install requests)  
#### 以下指令请在在后端目录中运行指令！
### 初次部署指令：
 set FLASK_APP=app.py（Windows系统）  
 export FLASK_APP=app.py（Linux系统）
### 启动指令：
 flask run --host='0.0.0.0'  
 或者  
 flask run --host='0.0.0.0' --post=8000(8000指端口号，默认为5000端口，可以自行改）
### 管理key  运行admin_key.py
 新增key：makenewkey 【IP】  
 更改key：changekey 【IP】  
 自定义更改key：changekey 【IP】 【key】  
