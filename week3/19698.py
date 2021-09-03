import sys

N,W,H,L=map(int,sys.stdin.readline().split())

cnt=(W//L)*(H//L)

print(cnt)