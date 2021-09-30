import sys

n=int(sys.stdin.readline())

case1=int("12"*n)
case2=int("21"*n)

data=int(sys.stdin.readline())


if (data==case1) or (data==case2):
    print("Yes")
else:
    print("No")