num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

print("You entered:", num1, num2, num3, num4)

addition_result = num1 + num2
print("Sum of", num1, "and", num2, "is:", addition_result)

subtraction_result = num3 - num4
print("Difference between", num3, "and", num4, "is:", subtraction_result)

multiplication_result = num1 * num2 * num3 * num4
print("Product of all numbers is:", multiplication_result)

division_result = (num1 * num2) / (num3 + num4)
print("Division of product of first two numbers by sum of last two numbers is:", division_result)

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)