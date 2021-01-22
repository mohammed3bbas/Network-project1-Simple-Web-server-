import socket
def viewpage(path):
    if (path == '/1'):
        response = f"<!DOCTYPE html><html lang='en'><head> <meta charset='UTF-8'> <title>ENCS436 Webserver</title></head><body><p style='text-align: center;'>ENCS431 2020/2021</p><p style='text-align: center;'>Welcome to Our Server</p><p style='text-align: center;'><strong>Tarek Khoury 1173019</strong></p><p style='text-align: center;'><strong>Mohammad Abbas 1170011</strong></p><p style='text-align: center;'>Welcome to our course <span style='color: rgb(0, 255, 0);'>Computer Networks</span></p><p style='text-align: center;'>Client IP address:{address[0]}</p><p style='text-align: center;'>Client Port Number:{address[1]}</p></body></html>".encode()
        header = 'HTTP/1.1 200 OK\n' + 'Content-Type: text/html \n\n'
    elif (path == '/2'):
        file = open('view1.html', 'rb')
        response = file.read()
        file.close()
        header = 'HTTP/1.1 200 OK\n' + 'Content-Type: text/html \n\n'
    elif (path == '/3'):
        file = open('16.jpg', 'rb')
        response = file.read()
        file.close()
        header = 'HTTP/1.1 200 OK\n' + 'Content-Type: image/jpg \n\n'
        # print(header)
    else:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode()
        # print(header)
    connection.send(header.encode() + response)
    connection.close()
def get_path(request):
    try:
        l= request.split(' ')
        return l[1]
    except :
        return "error"

#first we define the HOST and port number
HOST= '0.0.0.0'
PORT= 7000
#here we open a socket (TCP connection)
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((HOST, PORT))
ServerSocket.listen(1)
print('webserver serving on port: ', PORT)

while True:
    #here we make a conncection and get the address of the client
    connection, address = ServerSocket.accept()
    ip, port = ServerSocket.getsockname()
    #decode as 8 bit  characters
    request = connection.recv(1024).decode()
    print("------------------------------------------------------------------")
    print(request)
    print("------------------------------------------------------------------")
    #get the path
    path = get_path(request)
    viewpage(path)






