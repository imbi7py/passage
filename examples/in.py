import socket
from passage.way import Passageway
from passage.connections import connect

outbound = connect('/tmp/socket')

pw = Passageway()

sock = pw.obtain(outbound, socket.socket)
bytes_received = sock.recv(64)
print bytes_received, '... from', sock
sock.close()
