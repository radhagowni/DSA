# this is to find the index of pairs of numbers in which their sum must be equals to k.
n,k=map(int,input().split())
a=list(map(int,input().split()))
f=0
r=n-1
while(f<r):
    s=a[f]+a[r]
    if s==k:
        print(f,r)
        break
    elif s<k:
        f=f+1 
    else:
        r=r-1 
else:
    print(-1)
