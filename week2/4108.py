import sys

#함수제작
def plus(arr,x,y):
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if type(arr[i][j])==int:
                arr[i][j]+=1
    arr[x][y]='*'



while True:
    R,C=map(int,sys.stdin.readline().split())
    if R==0 and C == 0:
        break
    box=[]
    result=[[0]*(C+2) for i in range(R+2)]
    for i in range(R):
        box.append(sys.stdin.readline().rstrip())

    line=-1
    for data in box:
        bomb=list(filter(lambda x:data[x] == '*',range(len(data))))
        line+=1

        for i in bomb:
            plus(result,line+1,i+1)

    for i in range(1,R+1):
        print(*result[i][1:C+1],sep='')
    


