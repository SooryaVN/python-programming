a=int(input())
b=0
c=1
for i in range(0,a):
    print(c,end=" ")
    sum=b+c
    b=c
    c=sum
