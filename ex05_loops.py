n = int(input("Enter an integer n: "))

# Loop from 0 to n (inclusive, so we use n + 1)
for i in range(n + 1):
    # Check if the number is even
    if i % 2 == 0:
        print(i)