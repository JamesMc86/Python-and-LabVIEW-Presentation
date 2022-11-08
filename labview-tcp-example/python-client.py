import socket
import numpy as np
import matplotlib.pyplot as plt


TCP_IP = '127.0.0.1'
TCP_PORT = 6340

dt = np.dtype(np.float64)
dt = dt.newbyteorder('>')

x = np.arange(0, 50)
y = np.zeros((50, 1))
plt.ion()
fig = plt.figure()
line, = plt.plot(x,y)
plt.ylim(0.0, 1.0)
plt.show()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

try:
    while(True):
        size = int.from_bytes(s.recv(4), byteorder="big")
        data = s.recv(size)
        y = np.frombuffer(data, dtype=dt)
        line.set_data(x, y)
        plt.pause(0.1)
except KeyboardInterrupt:
    pass

s.send(b"Q")
s.close()

print("received data:", y)