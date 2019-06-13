import socket
scobj=socket.socket()
scobj.bind(('10.1.8.34',8086))
scobj.listen(1)
print('server running...')
conn,addr=scobj.accept()
conn.send('connection succes in server'.encode())
while True:
    print('waiting for msg')
    data=conn.recv(1024)
    if data:
        print('msg recieved',data.decode())
        msg=input('enter msg')
        conn.send(msg.encode('ascii'))
        if msg=='exit':
            break
conn.close()
