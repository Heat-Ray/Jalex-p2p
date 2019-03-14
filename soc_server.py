import socket               

def startServer(filePath):
   print("Server Started")
   filename = filePath.split('/')
   index = len(filename)
   filenameInBytes = filename[index-1].encode('utf-8')
   print(filename[index-1]+" "+str(index))

   s = socket.socket()
   host = '' # Get local machine name
   port = 12340                # Reserve a port for your service.
   s.bind((host, port))        # Bind to the port
   fl=open(filePath,'rb')   # Open file in binary mode to send
   d=fl.read(1024)             # Saves 1024 file bytes in list D

   s.listen(5)                 # Now wait for client connection.
   while True:
      c, addr = s.accept()     # Establish connection with client.
      print ('Got connection from', addr)
      c.send(filenameInBytes)
      while d!=b'':            # Executes till file list D is empty
         c.send(d)
         d=fl.read(10240)
      c.send(b'')
      c.close()                # Close the connection

