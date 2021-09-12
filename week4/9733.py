import sys

do={"Re":0,"Pt":0,"Cc":0,"Ea":0,"Tb":0,"Cm":0,"Ex":0}
data=[]
len_data=0

#입력
while True:
    d=list(map(str,sys.stdin.readline().split()))
    if not d:
        break
    data.append(d)

#개수 세주기
for i in data:
    for j in i:
        len_data+=1
        if j in do:
            do[j]+=1
        else:
            continue
    
#출력
for i,j in do.items():
    print("%s %d %0.2f" %(i,j,j/len_data))
print("Total %d 1.00" %(len_data))