#if index starts from 0 and fibonacci series starts from 0
# We have given different approches to find the same series
def fibonacci(n):
    l=[]
    a=0 
    b=1 
    for i in range(1,n):
        if i>1:
           c=a+b 
           a=b 
           b=c
           l.append(c) 
        else:
            l.append(a)
            l.append(b)
    return l[n-1]
n=int(input("Enter the value:"))
print(fibonacci(n))
