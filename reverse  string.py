# Python program to reverse a string word by word
s=input()
l=[]
for i in s.split():
    l.append(i)
l.reverse()
print(*l)

