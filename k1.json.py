import json
x=0
p={}
l1=[]
name=input("enter name :")
with open ("k.json","r")as f:
    k=json.loads(f.read())
    for i in k :
        print (i)
        ans = input ("enter the answer :")
        l1.append(ans)
        if ans ==k[i]:
            print("correct")
            x=x+1
        else:
            print("wrong")
            x=x-1
    p={name:l1}
    print(p)
    print(x)
