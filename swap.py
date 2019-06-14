h=list(input())
h[::2],h[1::2]=h[1::2],h[::2]
print(*h,sep="")

