#it is to find maximum element in an array
# the time complexity of this program will be O(n)
print("Enter the size of the array:")
n=int(input())
print("Enter ",n,"values:")
l=list(map(int,input().split()))
max_ele=l[0]
for i in range(1,n):
    if l[i]>max_ele:
        max_ele=l[i]

print("The maximum element in the array :",max_ele)


