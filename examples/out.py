import socket
from passage.way import Passageway
from passage.connections import bind

pw = Passageway()

listener = bind('/tmp/socket')
inbound, _ = listener.accept()

sock = socket.create_connection(('google.com', 80))
sock.sendall('GET http://google.com/ HTTP/1.0\r\n\r\n')
pw.transfer(inbound, sock)
sock.close()

print 'successfully transfered %r, exiting.' % sock
