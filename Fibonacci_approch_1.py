#fibonacci series upto value n 
n=int(input("Enter the value:"))
new_list=[1,1]
for i in range(n):
    if i>1:
        s=new_list[i-1]+new_list[i-2]
        new_list.append(s)
print("Fibonacci series:")
print(new_list[n-1])
