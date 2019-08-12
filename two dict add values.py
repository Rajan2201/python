# Python program to combine two dictionary adding values for common keys
d1={'a':200,'b':100,'c':300}
d2={'d':500,'c':700,'e':200}
for key in d2:
    if key in d1:
        d2[key]=d2[key]+d1[key]
    else:
        print("no common keys")
print(d2)
