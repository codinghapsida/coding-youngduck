for i in range(int(input())):
    d={}
    data=input().replace(" ","")
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    result=sorted(d.items(),key=lambda x:x[1],reverse=True)
    if len(result)>1:
        if result[0][1]==result[1][1]:
            print("?")
        else:
            print(result[0][0])
    else:
        print(result[0][0])
