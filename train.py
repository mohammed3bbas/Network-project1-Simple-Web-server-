# import http.server
# import socketserver
#
#
# class MyHandler(http.server.SimpleHTTPRequestHandler):
#     def handle_one_request(self):
#         # print("11")
#         print(self.client_address[0])
#         # return SimpleHTTPServer.SimpleHTTPRequestHandler.handle_one_request(self)
#
# print("Serving local directory")
# httpd = socketserver.TCPServer(("", 8080), MyHandler)
#
# while True:
#     httpd.handle_request()
import http.server
import socketserver
from socket import *
from urllib import response


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/1':
            self.path = 'view1.html'
        elif self.path =='/2':
            self.path = 'view2.html'
        elif self.path== '/3':
            self.path='16.jpg'
        # return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def client_ip(self):
        print(http.server.SimpleHTTPRequestHandler.client_address[0])
# Create an object of the above class
handler_object = MyHttpRequestHandler
# print(handler_object.client_address[0])
PORT = 7000
# # Star the server

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(httpd.server_address)
    # handler_object.client_ip(handler_object)
    httpd.serve_forever()
#
# #---------------------------------------------
# # from socket import *
# # serverPort = 7000
# # serverSocket = socket(AF_INET,SOCK_STREAM)
# # serverSocket.bind(('127.0.0.1',serverPort))
# # serverSocket.listen(1)
# # print ('The server is ready to receive')
# # while True:
# #      connectionSocket, addr = serverSocket.accept()
# #      print(addr)
# #      sentence = connectionSocket.recv(1024).decode()
# #      capitalizedSentence = sentence.upper()
# #      connectionSocket.send(response.encode())
# #      connectionSocket.close()
# from socket import *
#
# serverPort = 12000
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(('', serverPort))
# serverSocket.listen(1)
# print ('The server is ready to receive')
# while True:
#     connectionSocket, addr = serverSocket.accept()
#     sentence = connectionSocket.recv(1024).decode()
#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence.encode())
#     connectionSocket.close()
# import socket
#
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket.bind(("localhost", 7000))
# serversocket.listen(1)
#
# msg = '<!DOCTYPE html>'+ '<html>' + '<head>'+' <title>ENCS436 Webserver</title>'+ '</head>'+ '<body>'+ '<h1><b>Name : mohammad abbas  <p>ID : 1170011</p></b></h1>'+ '<h2>Welcome to our course <big style="color:green;">Computer Networks</big></h2>'+ '</body>'+ '</html>'
#
# (clientsocket, address) = serversocket.accept()
# sent = clientsocket.send("<title> ENCS436 </title>")