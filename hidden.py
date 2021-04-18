import os
from cryptography.fernet import Fernet
import time
key = ''
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
if(os.path.isfile('./password.txt') and os.path.isfile('./key.key')):
    with open('./key.key','rb') as file_key:
        key = file_key.read()
    desencriptado('./password.txt',key)
    with open('./password.txt','r') as txt:
        password = txt.read()
    encriptado('./password.txt',key)
    while True:
        getPass = input('Password: ')
        if(getPass != password):
            print('Contraseña incorrecta')
        else:
            break
def createKey():
    def generateKey():
        key = Fernet.generate_key()
        with open('key.key','wb') as file:
            file.write(key)
    def loadKey():
        return open('key.key','rb').read()
    generateKey()
    return loadKey()
enc_or_dec = False
while True:
    dir = os.listdir('./')
    folders = []
    if(os.path.isfile('./key.key') == True):
        with open('./key.key','rb') as file_key:
            key = file_key.read()
        print('Desencriptar: 1') 
        print('Salir: 2')
        res = input('')
        if(res == '1'):
            print(key)
            enc_or_dec = False
        elif(res == '2'):
            exit()
    else:
        enc_or_dec = True
        print('Encriptar: 1')
        print('Salir: 2')
        res = input('')
        if(res == '1'):
            key = createKey()
        elif(res == '2'):
            exit()
    in_folders = False
    for file in dir:
        root,extension = os.path.splitext(file)
        print(file)
        if(extension):
            if(str(root) != 'hidden' and str(root) != 'key'):
                if(enc_or_dec):
                    encriptado(file,key)
                    print(str(file)+' encriptado!.')
                else:
                    desencriptado(file,key)
                    print(str(file)+' desencriptado!.')
        else:
            folders.append(root)
    time.sleep(1)
    n = 0
    if(len(folders) > 0):
        in_folders = True
        for folder_name in folders:
            dir = os.listdir('./'+folder_name)
            for file in dir:
                file_dir = folder_name+'/'+file
                root,extension = os.path.splitext(file_dir)
                if(extension):
                    if(enc_or_dec):
                        encriptado(file_dir,key)
                        print(str(file_dir)+' encriptado!.')
                    else:
                        desencriptado(file_dir,key)
                        print(str(file_dir)+' desencriptado!.')
            n = n+1
            if(n == len( folders)):
                in_folders = False
    if(enc_or_dec == False and in_folders == False):
        os.remove('./key.key')