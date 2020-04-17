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
