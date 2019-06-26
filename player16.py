x=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
  if(x.count(i)>1):
    y.append(i)
  else:
    print(i)
