x=list(input())
y=0
for i in x:
  c=x.count(i)
  if y<c:
    y=c 
    s=i
print(s)   
