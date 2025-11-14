# reversing the words in a string
def reverseWords(s):
    s=s.strip()
    ar=list(map(str,s.split(" ")))
    t=''
    for i in range(len(ar)-1,-1,-1):
      if ar[i]=='':
        continue
      else:
         t+=ar[i]
         if i!=0:
           t=t+" "
    return  '"'+t+'"'
s=input()
print(reverseWords(s))
