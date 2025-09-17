num=int(input())
if num < 2: 
    print(False) 
else:
        s = 0
        for i in range(1,int(n/2)+1):
            if num % i == 0:
                s += i
            
if  s == num:
    print(True)
else:
    print(False)