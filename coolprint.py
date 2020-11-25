import math
import time

def getKey(item):
    return item[0]

def theprint(text1,text2,text3,n):
    t = 0
    pos1 = 0
    pos2 = n/2
    pos3 = n/4
    middle = int(n/2)
    text4 = ""
    while True:
        t += 0.01
        pos1 =  int(n/2 + 1 + n/2*math.cos(7*t))
        pos2 =  int(n/2 + 1 + n/2*math.cos(10*(t+math.pi/2)))
        pos3 =  int(n/2 + 1 + n/2*math.cos(5*(t+math.pi/4)))
        l = [(pos1,text1),(pos2,text2),(pos3,text3),(middle,text4)]
        sortl = sorted(l,key=getKey)
        print(" " * sortl[0][0] + sortl[0][1] + " "*(int(sortl[1][0] - sortl[0][0])) + sortl[1][1]+ " "*(int(sortl[2][0] - sortl[1][0])) + sortl[2][1]+ " "*(int(sortl[3][0] - sortl[2][0])) + sortl[3][1])
        time.sleep(0.02)



    
theprint("ll","pp","mm", 150)

#print(" " * pos1 + text1 + " "*(int(n - po s1)))