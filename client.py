import socket
scobj=socket.socket()
host='10.1.1.112'
port=8888
scobj.connect((host,port))
print(scobj.recv(1024).decode())
scobj.close()
