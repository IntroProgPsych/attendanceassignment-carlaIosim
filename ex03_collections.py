
user_input = input("Enter 5 integers separated by spaces: ")


numbers = [int(x) for x in user_input.split()]

counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1


print(numbers)


print(counts)