from socket import *

host = ''
port = 8000

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
while True:
      message = raw_input("Your Message: ")
      s.send(message)
      reply = s.recv(1024)
      print "Received", repr(reply)

s.close()
