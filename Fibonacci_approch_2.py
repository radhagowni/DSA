#fibonacci series using a function called fibonacci
def fibonacci(n):
    l=[]
    a=1 
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
print("Fibanacci series using functions:")
print(fibonacci(n))
