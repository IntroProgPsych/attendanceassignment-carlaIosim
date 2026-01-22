score = int(input("Enter score (0-100): "))


if score < 0 or score > 100:
    print("invalid")
elif score < 50:
    print("fail")
elif score <= 79: # Covers 50-79 because <50 was already caught
    print("pass")
else: # Covers 80-100
    print("excellent")