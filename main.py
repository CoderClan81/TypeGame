import os
import time
import usefuls
import enemy
from datetime import datetime

pretext=["WAR IS HERE!!",'Save Yourself!!','RETRIEVE','Soldier!!','You have entered in the Enemy Teritory!']
usefuls.prin(pretext)
U_name=str(input("Enter your name to excess the information!\n"))

os.system('cls')
intro=['Reporting to:','Captain '+U_name ,'The situation is getting worst','Most of our soldiers have died','The rest have retrieved','Supporting forces are on their way','But need some time','Till then...','You have to ristrict the enemy forces from entering the base','Our hope depends on You!!' ]
rules=['Each enemy will enter in the base with a codenumber','Code number of current enemy will be displayed when he will enter','Entering the codenumber in the console will decrease their health status','If the health reaches zero, the enemy will die!!']
layer=['The attack will take place in 4 waves','To tackle a wave, you will have a limited span of time','If you succeeded in killing them all,','You will survive to face the next battle','ELSE','Your SOUL WILL REST IN PIECE....','']
cong=['Congratulations '+'Captain '+U_name]
health=[3,5,8,60]
lay=[1,2,3,4]
e_nu=[10,8,6,1]
late=[5,5,4,4]

usefuls.prin(intro)
time.sleep(2)
usefuls.prin(rules)
time.sleep(2)
while True:
    usefuls.prin(layer)
    time.sleep(2)
    flag=1
    score=0

    for l in lay:
        l_text=['Here comes the wave number '+str(l),'Enemies:  '+str(e_nu[l-1]),'Healthspan:   '+str(health[l-1]),'time limit: '+str(late[l-1])+' minutes','ALL THE BEST CAPTAIN!!']
        usefuls.prin(l_text)
        time.sleep(3)
        e_c=e_nu[l-1]
        da=datetime.now()

        while e_c>0:
            act=-1
            ene=enemy.Enemy(l,health[l-1])
            #print('codenum: ',ene.codenum)
            usefuls.codePrin(ene.codenum)

            while (flag is 1) and (act is -1):
                c=int(input(""))
                act=ene.attack(c,da)
                if act is -2:
                    flag=0
                    break
                elif act>=0:
                    e_c-=1

            if flag is 0:
                break

        if flag is 0:
            print("Game Over!!\n Your score is: ",score)
            break
        else:
            print("Attack is successfully tackled.!!\n")
            score+=act
            print("Your score now: ",score)

    if flag is 1:
        usefuls.prin(cong)
    k=str(input("Do you want to play again??\n press\nY: Yes\n N: No\n"))
    if k is 'N':
        break
