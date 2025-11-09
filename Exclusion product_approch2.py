#approch2 for exclusion product calculation
n=int(input())
arr=list(map(int,input().split()))
mod=(10**9)+7
res=[1]*n
left=1
for i in range(n):
    res[i]=left
    left=(left*arr[i])%mod
right=1
for i in range(n-1,-1,-1):
    res[i]=(res[i]*right)%mod
    right=(right*arr[i])%mod
print(*res)
