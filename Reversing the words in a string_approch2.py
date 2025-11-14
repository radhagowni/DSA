# simple code to reverse the words in a string
def reverseWords(s):
       return ' '.join(reversed(s.split()))
s=input()
print(reverseWords(s))
