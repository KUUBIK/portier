# import socket
#
# def Main():
#     host = ("10.101.15.128")
#     port = 8888
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host, port))
#
#     filename = input("Filename? -> ")
#     if filename != 'q':
#         s.send(filename.encode())
#         data = s.recv(1024)
#         if data[:6] == 'EXISTS':
#             filesize = long(data[6:])
#             message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
#             if message == 'Y':
#                 s.send("OK")
#                 f = open('new_'+filename, 'wb')
#                 data = s.recv(1024)
#                 totalRecv = len(data)
#                 f.write(data)
#                 while totalRecv < filesize:
#                     data = s.recv(1024)
#                     totalRecv += len(data)
#                     f.write(data)
#                     print ("{0:.2f}").format((totalRecv/float(filesize))*100)+ "% Done"
#                 print ("Download Complete!")
#                 f.close()
#         else:
#             print ("File Does Not Exist!")
#
#     s.close()

import socket
import sys

s = socket.socket()
s.connect(("192.168.8.100",8888))
f = open("/home/robert/androidflask/projectfolder/tests.zip", "rb")
print(f)

l = f.read(4096)
while (l):
    s.send(l)
    l = f.read(4096)
s.close()
