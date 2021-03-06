#ID   :H20191030124
#Name :Geetika Joshi

import socket 
    
from _thread import *
import threading 
user_hash={}
print_lock = threading.Lock() 
import hashlib, binascii, os

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def threaded(c,addr): 
    passk = c.recv(1024) 
    print(passk.decode('ascii'))
    hashed = hash_password(passk.decode('ascii'))
    user_hash[addr]=hashed
    print(user_hash)
    while True: 
        data = c.recv(1024)
        if not data: 
            #print("Hello456")
            print('Bye') 
            #print_lock.release() 
            break
        data = data[::-1]  
        c.send(data) 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(5) 
    print("socket is listening") 
    while True:  
        c, addr = s.accept() 
        #print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,addr[1],)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 