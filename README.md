# Network-Security-Socket-programming
Question 1 : Implement a client-server program which will facilitate a client to register itself to the server.

The file is contained inside a folder named Task-3 which include server and client codes for this task.

The server code is named as : T3SERVER.py
The client code is named as : T3CLIENT.py

For this we write a server code and a client code.The server can be connected to multiple clients using threads.
We have a function which stores the hashed value of the password of the different clients.
The client program connects with server using sockets and registers it's password.

Question 2 : Every registered client must declare its public key to the server during registration phase. Any registered client can request separately the public key of any other registered client and the server will supply the corresponding public key.  Request of public key can be made several times.

The file is contained inside a folder named Task-4 which include server and client codes for this task.

The server code is named as : T4SERVER.py
The client code is named as : T4CLIENT.py

In this clients get each other information through the server.The client enters the key for that client for which it wants public key.

