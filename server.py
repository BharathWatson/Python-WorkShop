import socket
scobj=socket.socket()
host="10.1.8.34"
port=8888
scobj.bind((host,port))
scobj.listen(10)
while True:
    conn,addr=scobj.accept()
    print("connected from ",addr)
    msg="you are now connected"
    conn.send(msg.encode())
    conn.close()
    
