import random
import usefuls

class Enemy:
    lifespan=0
    wave=0
    codenum=0
    dialogue=['opps!!','Your time is over pal! :P','See you in the hell!!']
    def __init__(self,x,h):
        self.wave=x
        self.lifespan=h
        r=x*100
        self.codenum=random.randrange(r+1,10*r-1)
    def attack(self,num,da):
        time_rem=usefuls.timecheck(da,self.wave)
        if time_rem>=0:
            if self.codenum == num :
                print('ouch!!')
                self.lifespan-=1
                if self.lifespan is 0 :
                    return int(time_rem)
                else:
                    return int(-1)
            else:
                print('HAHA!! You missed it moron! :P it\'s',self.codenum)
                self.lifespan+=1
                return int(-1)
        else:
            usefuls.prin(self.dialogue)
            return int(-2)
