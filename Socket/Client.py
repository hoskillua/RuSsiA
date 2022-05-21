# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 22222               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
while True:
    
    # receive data from the server and decoding to get the string.
    print ("response:"+s.recv(1024).decode())
    
    msg = input("message:")
    s.send(msg.encode())
    
    if msg == 'end':
        s.close() 
        break
 