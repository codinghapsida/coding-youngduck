import sys

n,m=map(int,sys.stdin.readline().split())

result=n

while n>=m:
    n=n//m
    result+=n


print(result)