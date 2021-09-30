import os
import re
from cryptography.fernet import Fernet
key = ''
path = './'
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
if(os.path.isfile(path+'password.txt') and os.path.isfile(path+'key.key')):
    with open(path+'key.key','rb') as file_key:
        key = file_key.read()
    desencriptado(path+'password.txt',key)
    with open(path+'password.txt','r') as txt:
        password = txt.read()
    encriptado(path+'password.txt',key)
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
    if(os.path.isfile(path+'key.key') == True):
        with open(path+'key.key','rb') as file_key:
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
    for root, directories, files in os.walk(path):
        for name in files:
            if not re.search('node_modules',root) and not re.search('.git',root):
                if not name == 'hidden.exe' and not name == 'key.key' and not name == 'hidden.py':
                    pathFile = os.path.normpath(root + "/" + name)
                    if(enc_or_dec):
                        encriptado(pathFile,key)
                        print(str(pathFile)+' encriptado!.')
                    else:
                        desencriptado(pathFile,key)
                        print(str(pathFile)+' desencriptado!.')
    if(enc_or_dec == False):
        os.remove('./key.key')