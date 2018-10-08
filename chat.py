from socket import *

host = ''

port = 8000

s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

print 'connected by' , addr
while True:
      data = conn.recv(1024)
      print "Received" , repr(data)
      reply = raw_input("Reply: ")
      conn.sendall(reply)

conn.close()
