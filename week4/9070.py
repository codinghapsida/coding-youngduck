for t in range(int(input())):
    data=[]
    for n in range(int(input())):
        #data=[중량,가격,가성비]
        w,c=map(int,input().split())
        data.append([w,c,w/c])
    data=sorted(data,key=lambda x:(x[2],-x[1]),reverse=True)
    print(data[0][1])
    
       