# first of all import the socket library
import socket   
import pickle         
from RSA import *
#intialzing RSA
rsa = RSA(p=101, q=103, e=11)
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 22222               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
while True:
    
    
    
    msg = input("Client:")
    encryptedList = rsa.Encrypt(msg)
    print(encryptedList)
    encryptedMsg = "NIGGER".join( [ConvertToStr(c) for c in encryptedList])
    
    strArray = encryptedMsg.split("NIGGER")
    encryptedList = [ConvertToInt(c) for c in strArray]
    msg = rsa.Decrypt(encryptedList)
    print(msg)
    s.send(encryptedMsg.encode())
    
    if msg == 'end':
        s.close() 
        break

    # receive data from the server and decoding to get the string.
    print (s.recv(4096).decode())
 