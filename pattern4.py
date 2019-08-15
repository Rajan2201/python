#python program to print the pattern
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
for i in range(0,5):
    for j in range(0,5-i):
        print("*",end="")
    for j in range(0,5-i):
        print(end=" ")
        print(" ")
    print()
