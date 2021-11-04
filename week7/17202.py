import sys
import heapq

a=list(sys.stdin.readline().rstrip())
b=list(sys.stdin.readline().rstrip())
data=[]

#초기 세팅
for i in range(8):
    data.append(int(a[i]))
    data.append(int(b[i]))

for i in range(14):
    data[i]