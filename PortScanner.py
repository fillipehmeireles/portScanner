import socket
from threading import Thread

host=input("host>")
from_port=int(input("start scan from port>"))
to_port=int(input("finish scan to port>"))
couting_open=[]
couting_close=[]
threads=[]

def scan(port):
    s=socket.socket()
    result=s.connect_ex((host,port))
    print("working on port>"+str(port))
    if result==0:
        couting_open.append(port)
        print(str(port)+"-> open")
        s.close()
    else:
        couting_close.append(port)
        print(str(port)+"-> close")
        s.close()

for i in range(from_port,to_port+1):
    t=Thread(target=scan,args=(i,))
    threads.append(t)
    t.start()
    if i==to_port+1:
        t.close()

print("###############")
print("Opened Doors")
print(couting_open)
print("Good Luck :)")
print("###############")
print("Developed By Fillipe Henrique")
