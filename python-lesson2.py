limit=int(input("Enter a number: "))
count=0

for num in range(5, limit +1, 3): # Only even numbers
    count += 1
print(" Total of even numbers up to", limit, "is:", count)    