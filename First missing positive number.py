t=int(input())
for i in range(t):
   n=int(input())
   arr=list(map(int,input().split()))
   arr=[x for x in arr if x>0]
   if not arr:
     print(1)
     continue
   arr=sorted(set(arr))
   if arr[0]!=1:
      print(1)
      continue
   missing=-1
   for i in range(len(arr)-1):
      if arr[i+1]!=arr[i]+1:
        missing=arr[i]+1
        break
   if missing==-1:
      print(arr[-1]+1)
   else:
      print(missing)
