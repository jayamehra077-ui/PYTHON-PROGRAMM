//write a program to take input and check prime or not//
n=int(input("enter number to check prime or not: "))
if n<=1:
    print("invalid input")
else:
    for i in range(2,n+1):
       if n%i==0:
        print("not a prime number")
        break
    else:
        print("prime")
    
    



