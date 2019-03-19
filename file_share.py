import socket
import threading

def starts_connection_server(file_n):
    print(10)
    s = socket.socket()
    host = ''
    port = 40555
    s.bind((host, port))
    
    fl=open(file_n,'rb')   
    d=fl.read(10240)
    
    file_n_list = file_n.split('/')
    index = len(file_n_list)
    filenameInBytes = file_n_list[index-1].encode('utf-8')
    
    s.listen(1)
    
    c , addr=s.accept()
    c.send(filenameInBytes)
    while d!=b'':            
         c.send(d)
         d=fl.read(10240)
    c.send(b'')
    c.close()  
    

def starts_listening_client(l):
    print(11)
    s = socket.socket()
    host = socket.gethostname()
    port = 40555
    s.connect((host,port))

    filenameInBytes = s.recv(1024)
    file_ka_naam = filenameInBytes.decode('utf-8')
    
    fl=open(file_ka_naam,'wb')   
    d=s.recv(10240)              
    while d!=b'':
        l.acquire()
        fl.write(d)
        d=s.recv(10240)
        l.release()
    fl.close()
    s.close()
    
    
