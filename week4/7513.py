import sys

for t in range(int(sys.stdin.readline())):
    data=[]
    print("Scenario #%d:" %(t+1))
    for m in range(int(sys.stdin.readline())):
        data.append(sys.stdin.readline().rstrip())
    # password=[print(data[k],end='') for n in range(int(sys.stdin.readline())) for k in list(map(int,sys.stdin.readline().split()))[1:]]
    for n in range(int(sys.stdin.readline())):
        key=list(map(int,sys.stdin.readline().split()))
        for k in key[1:]:
            print(data[k],end='')
        print('')
    print('')


