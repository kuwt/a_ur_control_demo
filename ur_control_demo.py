import socket
import numpy as np
import datetime
import time

HOST = "10.6.88.81"  # depends on network setup of ur3
PORT = 30002  # the same port as used by the server



def gen_script():
    # prepare the script to be sent to robot

    script = ''
    script += 'def PriamryProgram():' + '\n'
    t = 10. #sec
    x = 0.  #m
    y = -0.233
    z = 0.05
    rx = 2.7 #rad
    ry = 1.7
    rz = 0.
    
    script += 'servoj(get_inverse_kin(p[{},{},{},{},{},{}]),t = {})'.format(x,y,z,rx,ry,rz,t)
    script += '\n'

    v = 0.1  # velocity
    a = 1.2  # acceleration
    #script += 'movej(p[-0.088, -0.316, 0.4, 0, 3.147, 0], a=1.2, v=0.1)' + '\n'         
    #script += 'sleep(0.5)' + '\n'

    script += 'end' + '\n'
    print(script)

    return script



script = gen_script()

print('3s to run')
time.sleep(1)
print('2s to run')
time.sleep(1)
print('1s to run')
time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(script.encode(encoding='utf_8', errors='strict'))

data = s.recv(1024)
s.close()

print("Received", repr(data))