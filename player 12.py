x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
z=''
for i in range(0,x[1]):
  y = [y[-1]] + y[:-1]
print(*y,sep=' ')
