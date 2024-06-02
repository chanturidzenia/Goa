def calculate_future_ages(ages):
    future_ages = [age + 20 for age in ages]
    return future_ages

family_members = {
    "me": 17,
    "mother": 38,
    "father": 39,
    "sister1": 9,
    "sister2": 5,
    "brother": 7,
    "grandma": 56,
    "grandpa": 57
}

print("Current ages:")
for member, age in family_members.items():
    print(f"{member.capitalize()}: {age}")

future_ages = calculate_future_ages(family_members.values())

print("\nAges in 20 years:")
for member, age in zip(family_members.keys(), future_ages):
    print(f"{member.capitalize()}: {age}")




def main():
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
gmail = input("Enter your Gmail address: ")


user_info = f"My name is {name} {surname}. I am {age} years old, currently living at {address}, and my Gmail address is {gmail}."

print(user_info)

if __name__ == "__main__":
    main()







