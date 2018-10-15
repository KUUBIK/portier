
#
# import socket
# import sys
# import os
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("192.168.1.87",8888))
# s.listen(10) # Acepta hasta 10 conexiones entrantes.
#
# while True:
#     s, address = s.accept()
#
#     print ('client connected:!', address)
#     i=1
#     f = open('zhami' + ".png",'wb') #open in binary
#     i=i+1
#     while (True):
#     # recibimos y escribimos en el fichero
#
#         l = s.recv(1024)
#         while (l):
#                 f.write(l)
#                 l = s.recv(1024)
#
#     # file = open('zhami.png', 'wb')
#
#     s.close()
#
#

#если поменять какое либо значение сохранить и снова его вернуть и так же сохранить то файл сможет снова передаться по tcp
from flask import Flask
import socket
import sys
import threading
import shutil
import datetime
import subprocess
app = Flask(__name__)
def launchServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.8.100",8888))
    s.listen(10)
    while True:
        s, address = s.accept()

        print ('client connected:!', address)
        i=1
        e=++i
        f = open('client' + str(e) + ".zip",'wb')
        while (True):
                l = s.recv(4096)
                shutil.move("/home/robert/androidflask/client1.zip", "/home/robert/androidflask/test/client3.zip") #некоторые файлы плохо грузятся (серая непрогрузка) т.к. неправильно расположен shutil.move
                while (l):
                        f.write(l)
                        l = s.recv(4096)
                        subprocess.call('unzip client3.zip', shell=True)
    s.close() #дабы не было ошибки bad file deskriptor просто убираем закрывающую функцю из цикла while

@app.route('/')
def hello_world():
    return '<H2>rombo!<H2>'
if __name__ == ("__main__"):
    t = threading.Thread(target=launchServer)
    t.daemon = True
    t.start()
    app.run("192.168.8.100", port=8080, debug=True)

############################################### Правильный и рабой сервак tcp на flask #####
# from flask import Flask
# import socket
# import sys
# import threading
# import shutil
# import datetime
# app = Flask(__name__)
# def launchServer():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(("192.168.1.123",8888))
#     s.listen(10)
#     while True:
#         s, address = s.accept()
#
#         print ('client connected:!', address)
#         i=1
#         e=++i
#         f = open('client' + str(e) + ".zip",'wb')
#         while (True):
#                 l = s.recv(4096)
#                 shutil.move("/home/robert/androidflask/client1.zip", "/home/robert/androidflask/test/client3.zip") #некоторые файлы плохо грузятся (серая непрогрузка) т.к. неправильно расположен shutil.move
#                 while (l):
#                         f.write(l)
#                         l = s.recv(4096)
#
#     s.close() #дабы не было ошибки bad file deskriptor просто убираем закрывающую функцю из цикла while
#
# @app.route('/')
# def hello_world():
#     return '<H2>rombo!<H2>'
# if __name__ == ("__main__"):
#     t = threading.Thread(target=launchServer)
#     t.daemon = True
#     t.start()
#     app.run("192.168.1.123", port=8080, debug=True)
