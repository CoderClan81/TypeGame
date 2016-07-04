import time
from datetime import datetime

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
