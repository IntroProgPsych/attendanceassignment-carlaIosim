
def clamp_rating(x):
    if x < 1:
        return 1
    elif x > 5:
        return 5
    else:
        return x


user_val = int(input("Enter a value: "))


result = clamp_rating(user_val)

# Print the result
print(result)