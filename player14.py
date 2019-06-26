x=int(input())
y=input()
temp=0
z=['a','e','i','o','u']
for i in z:
  if(i in z):
    y=y.replace(i,'')
print(y[::-1])
