a,b=list(map(int,input().split()))  
for i in range(a,b):  
   sum=0  
   temp=i 
   while temp > 0:  
       d=temp%10  
       sum+=d**3  
       temp//=10  
       if i==sum:  
            print(i,end=' ')  
