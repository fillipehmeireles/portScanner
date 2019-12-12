import sys
import socket
from threading import Thread

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


host= sys.argv[1]
from_port = int(sys.argv[3])
to_port = int(sys.argv[5])

couting_open=[]
couting_close=[]
threads=[]

if sys.argv[2] == 'f' and sys.argv[4] == 'to':
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
    print("Developed By Fillipe Henrique - LUSPEW")

else:
    print("'{f_param}' and  '{s_param}' are not valid, read more on https://luspew.com/blog/blog.php?id=portscanner".format(f_param=sys.argv[2],s_param=sys.argv[4]))


