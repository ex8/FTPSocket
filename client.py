import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6889

s.connect((host, port))

with open('test_file.txt', 'rU') as f:
    data = f.read(1024)
    print 'Sending file...',
    s.send(data)
    print 'OK'

s.close()
