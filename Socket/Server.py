# first of all import the socket library
import socket
import pickle   
from RSA import *

#intialzing RSA
rsa = RSA(p=101, q=103, e=11)

# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 22222               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  break

while True:

  msg = c.recv(4096).decode()
  strArray = msg.split("NIGGER")
  encryptedList = [ConvertToInt(c) for c in strArray]
  print(encryptedList)
  msg = rsa.Decrypt(encryptedList)
  print("server:"+msg)
  
  if(msg == "end"):
    c.send('Thank you for connecting'.encode())
    c.close()
    break
  c.send( ('Server recieved ' + msg).encode() )