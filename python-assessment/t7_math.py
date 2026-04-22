import math


# 1. Square roots of list

numbers = [1, 4, 9, 16, 25, 36]

print("Square Roots:")
for num in numbers:
    print(f"{num} -> {math.sqrt(num)}")



# 2. Factorials 1 to 10

print("\nFactorials (1 to 10):")
for i in range(1, 11):
    print(f"{i}! = {math.factorial(i)}")



# 3. Circle area (πr²)

r = 5
area = math.pi * (r ** 2)

print("\nCircle Area:")
print(f"Radius = {r}")
print(f"Area = {area}")



# Final neat output done
