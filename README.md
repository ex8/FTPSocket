# TCP Server/Client - File Transfer Protocol (FTP)
Simple file transfer protocol using TCP sockets.

# Requirements
Python 2.7+

# Usage
Run server and search for any port within server.py
```
python server.py
```
Output:
```
Server listening on port 6889...
```
Now run client.py on the same port
```
python client.py
```
The file will be received by the server through a socket connection.
