# Pandownload-fake-server
替代pandownload原本的服务器文件以绕过pandownload启动问题
这是一个傻瓜式教程

## 需求：
- python3 或者更高
- 一台服务器（推荐linux）
## 使用：
1. 下载该文件并解压

2. 这里边一共有两个文件夹，[Pandownload](/Pandownload/)为pandownload本体程序，而[pandownload-fake-server](/pandownload-fake-server/)为虚假服务器文件

3.
 - 方法1：将pandownload-fake-server文件夹打开找到目录下找到[pandownload-fake-server](/pandownload-fake-server/script.py),用记事本或者IDLE打开。应该能看到以下代码：
```
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"
 
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 80 #default port (you shouldn't be changing this one unless you know what you are doing)
server_address = ('127.0.0.1', port) #default ip address
 
HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)
 
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
```
找到
```
server_address = ('127.0.0.1', port) #default ip address
```
并且将这个ip地址改成所需要的ip地址

 - 方法2：如果想在同一台机子上运行该服务（此方法将不需要一台linux服务器）：
 找到[pandownload-fake-server](/pandownload-fake-server/)文件夹并在该目录下启动powershell然后输入：*注意：使用pandownload时请勿关闭该powershell窗口*
```
python -m http.server --bind 0.0.0.0 80
```

4.找到windows的hosts文件
路径：
```
C:\Windows\System32\Drivers\etc\hosts
```
修改该文件（用记事本打开）
向里面添加一行

```
[服务运行的ip地址（不含括号）] pandownload.com
```

例：
使用localhost（方法2）作为服务器：
```
127.0.0.1 pandownload.com
```
5.尝试启动pandownload
*祝阁下好运*

## 声明：
该程序以及文件仅供学习交流用，请勿作违法用途，作者不承担任何责任
