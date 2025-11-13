# program to find perfect approach
num=int(input())
if num < 2: 
    print(False) 
else:
        s = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num // i
            i += 1
if  s == num:
    print(True)
else:
    print(False)
