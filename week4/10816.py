import sys

n=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))

cnt={}
for i in card:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in data:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')
