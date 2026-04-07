//write a program to take input fom user and print all factors of input//
n=int(input("enter number: "))
odd=0
even=0
print("factors of given numbers is:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
        if i%2==0:
         even+=1
        else:
         odd+=1
print("odd factors are:",odd)
print("even factors are:",even)
