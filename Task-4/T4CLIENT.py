#ID   :H20191030124
#Name :Geetika Joshi

import socket 
  
  
def Main(): 
    host = '127.0.0.1'
    port = 12331
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port))
    print("Enter your passkey:") 
    Password_you_send_to_server = input()
    s.send(Password_you_send_to_server.encode('ascii'))
    while True:
        print("Enter User address to get the public key") 
        req = input()
        s.send(req.encode('ascii')) 
        data = s.recv(1024) 
        print('Received from the server :',str(data.decode('ascii'))) 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    s.close() 
  
if __name__ == '__main__': 
    Main() 