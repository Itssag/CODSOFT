import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*()><.,;:|"

# for length
length = int(input("Enter the length of Password\n"))


string = lower + upper + numbers + symbol

password = "".join(random.sample(string,length))

print("New Password is:" + password)

