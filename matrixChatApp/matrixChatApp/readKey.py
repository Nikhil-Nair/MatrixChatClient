import os
from matrixChatApp.settings import BASE_DIR

def extract():
    filePath = os.path.join(BASE_DIR,'key.txt')
    keyFile = open(filePath,'r')
    key = keyFile.read().rstrip()
    keyFile.close()
    return key
