import random

names_str = input("Input the names without separated commas:")
names = names_str.split()

who_pay = random.choice(names)

print(who_pay + " is going to pay the bill.")
