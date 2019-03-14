import socket               # Import socket module

def startClient():
    print("Client started")
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12340                # Reserve a port for your service.

    s.connect(('127.0.0.1', port)) # Change this to according to local ip.
    filenameInBytes = s.recv(1024)
    filename = filenameInBytes.decode('utf-8')
    filename = "Client" + filename
    fl=open(filename,'wb')   # Open file in binary mode to save
    d=s.recv(1024)              # Recieves 1024 bytes of data at once
    while d!=b'':               # Loop executes till recieved buffer is empty
        fl.write(d)
        d=s.recv(1024)
    fl.close()
    s.close()                     # Close the socket when done
