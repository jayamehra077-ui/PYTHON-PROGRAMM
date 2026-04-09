
def even_fac(n):
    ans = 1
    for i in range(2, n + 1, 2):
        ans *= i
    return ans

def odd_fac(n):
    ans = 1
    for i in range(1, n + 1, 2):
        ans *= i
    return ans

n = int(input("enter any number="))

if n % 2 == 0:
   
    
    print(odd_fac(n))
else:
  
    
    print(even_fac(n))
