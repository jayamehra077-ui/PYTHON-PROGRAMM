
n = int(input("Enter number: "))
# Store the original value for comparison
original_n = n 

# Step 1: Count total digits (c)
c = len(str(n))
ans = 0
temp = n

# Step 2: Calculate sum of digits raised to the power of c
while temp > 0:
    r = temp % 10
    ans += r ** c
    temp //= 10

# Step 3: Comparison
if ans == original_n:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")
