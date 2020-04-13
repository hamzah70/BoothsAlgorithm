import random

open('testcases.txt', 'w').close()

for i in range(20):
    x = random.randint(-1001, 1001)
    y = random.randint(-1001, 1001)
    with open('testcases.txt','a') as f:
        f.write(str(x)+" "+str(y)+'\n')
