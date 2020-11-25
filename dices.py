import matplotlib.pyplot as plt
import random 

def get_dictionnary(n,ndice):
    a = {}
    for i in range(n):
        add = 0
        for j in ndice:
            add += random.randint(1,j)
        if add not in a:
            a[add] = 1
        elif add in a:
            a[add] += 1
    return a

def draw(dic):
    plt.bar(dic.keys(), dic.values(), color='g')
    plt.show()



dic = get_dictionnary(100000,[6,6,8,4])
print(dic)
draw(dic)
