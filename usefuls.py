import time
from datetime import datetime
import os

def prin(lis):
    for l in lis:
        print(l)
        time.sleep(0.5)
def timecheck(da,w):
    m=0
    if w<3:
        m=5
    else:
        m=4
    m*=60
    n=datetime.now()
    s=(n-da).total_seconds()
    return int(m-s)
    
def codePrin(codenum)
    os.system('cls')
    print('')
    print('-'*40)
    for x in range (0,4)
        print('')
    print(' '*17,str(codenum))
    for x in range (0,4)
        print('')
    print('-'*40)
    time.sleep(2)

