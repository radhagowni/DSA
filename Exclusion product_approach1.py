n=int(input())
arr=list(map(int,input().split()))
mod=(10**9)+7
for i in range(n):
    prod=1
    for k in range(n):
        if k==i:
            continue
        else:
            prod=(prod*arr[k])%mod
    print(prod%mod,end=" ")