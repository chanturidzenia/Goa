#  3
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
num3 = input("Please enter the third number: ")
num4 = input("Please enter the fourth number: ")
num5 = input("Please enter the fifth number: ")

print(int(num1) + int(num2) + int(num3) + int(num4) + int(num5))
print(int(num1) - int(num2) - int(num3) - int(num4) - int(num5))
print(int(num1) * int(num2) * int(num3) * int(num4) * int(num5))
print(int(num1) / int(num2) / int(num3) / int(num4) / int(num5))
print(int(num1) % int(num2) % int(num3) % int(num4) % int(num5))
print(int(num1) // int(num2) // int(num3) // int(num4) // int(num5))

#  4
age = int(input("Please enter your age: "))

if age > 18 and age < 20:
    print("Your age is between 18 and 20.")

# Task 5
print(5 > 3)
print(2 < 8)
print(10 <= 10)
print(7 >= 5)
print(3 != 4)
print(6 == 6)

# 6
numi = input("Please enter the first number: ")
nume = input("Please enter the second number: ")

print(type(numi))
print(type(nume))

#  7
num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")

print(type(num1))
print(type(num2))

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
print(type(num1))
print(type(num2))

num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
print(type(num1))
print(type(num2))

print(num1 > 1 and num1 <= 10)

budget = int(input("Please enter your budget: "))
print(budget > 50 or budget > 100)
