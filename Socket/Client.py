# first of all import the socket library
from lib2to3.pytree import convert
import socket   
import pickle         
from RSA import *
#intialzing RSA


 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 22222               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
keyStr = s.recv(4096).decode()
key = keyStr.split("NIGGER")
n = ConvertToInt(key[0])
e = ConvertToInt(key[1])

while True:
    
    msg = input("Client:")
    encryptedList = Encrypt(msg, n, e)
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
 