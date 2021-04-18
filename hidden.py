import os
from cryptography.fernet import Fernet
import time
def generateKey():
    key = Fernet.generate_key()
    with open('key.key','wb') as file:
        file.write(key)
def loadKey():
    return open('key.key','rb').read()
generateKey()
key = loadKey()
def encriptado(fileName,key):
    f = Fernet(key)
    with open(fileName,'rb') as file:
        data = f.encrypt(file.read())
    with open(fileName,'wb') as file:
        file.write(data)
def desencriptado(fileName,key):
    f = Fernet(key)
    with open(fileName,'rb') as file:
        data = f.decrypt(file.read())
    with open(fileName,'wb') as file:
        file.write(data)
while True:
    print('Encriptar: #1')
    print('Desencriptar: #2')
    print('Salir: #3')
    res = input('')
    dir = os.listdir('./')
    folders = []
    for file in dir:
        root,extension = os.path.splitext(file)
        if(extension):
            if(str(root) != 'hidden' and str(root) != 'key'):
                if(res == '1'):
                    encriptado(file,key)
                    print(str(file)+' encriptado!.')
                elif(res == '2'):
                    desencriptado(file,key)
                    print(str(file)+' desencriptado!.')
                elif(res == '3'):
                    exit()
        else:
            folders.append(root)
    time.sleep(1)
    if(len(folders) > 0):
        for folder_name in folders:
            dir = os.listdir('./'+folder_name)
            for file in dir:
                file_dir = folder_name+'/'+file
                root,extension = os.path.splitext(file_dir)
                if(extension):
                    if(res == '1'):
                        print(file_dir)
                        encriptado(file_dir,key)
                        print(str(file_dir)+' encriptado!.')
                    elif(res == '2'):
                        desencriptado(file_dir,key)
                        print(str(file_dir)+' desencriptado!.')
                    elif(res == '3'):
                        exit()