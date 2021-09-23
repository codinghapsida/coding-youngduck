import sys
from itertools import combinations

fox=[1,3,4]
fox=list(combinations(fox,2))
cnt=0
for i in range(int(sys.stdin.readline())):
    finger=tuple(map(int,sys.stdin.readline().split()))
    
    if finger in fox:
        cnt+=1
        if cnt ==3:
            print("Wa-pa-pa-pa-pa-pa-pow!")
            break
    else:
        print("Woof-meow-tweet-squeek")
        break 



