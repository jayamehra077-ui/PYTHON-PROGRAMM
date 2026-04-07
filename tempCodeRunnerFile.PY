//write a program to take input fom user and print all factors of input
number=input("enter any number=")
factor=[]
for i in range(1,number+1):
   if (number%i==0):
    factor.append(i)
    return factor
