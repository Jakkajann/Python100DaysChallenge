import random

names_string = input("Give me everybody's names separated by a coma (,) ")

names = names_string.split(", ")

print(names)

length = len(names)
print(length)
random_person_number = random.randint(0, length - 1)

print(f"{names[random_person_number]} is who will pay the bill")