import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data.sort()

if n % 2 == 0:
    print(data[n//2-1])
else:
    print(data[n//2])