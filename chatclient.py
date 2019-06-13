import socket
scobj=socket.socket()
scobj.connect(('10.1.8.34',8086))
while True:
    data=scobj.recv(1024)
    if data:
        print('msg recieved',data.decode())
        msg=input('enter msg')
        scobj.send(msg.encode('ascii'))
        if msg=='exit':
            break
scobj.close()