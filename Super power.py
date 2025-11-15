#  to find super power of a number
def superPow(a, b):

    MOD = 1337
    ans = 1

    for i in b:
      ans = pow(ans, 10, MOD) * pow(a, i, MOD)

    return ans % MOD
a=int(input())
b=list(map(int,input().split()))
print(superPow(a,b))
