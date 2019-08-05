n=int(input("enter a number:"))
if n%400==0:
    print("it is a leap year")
elif n%100==0:
    print("it is not leap year")
elif n%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
