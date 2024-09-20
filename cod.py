import random
import string

low = string.ascii_lowercase
upp = string.ascii_uppercase
special = string.punctuation
nos = string.digits

str_all_letters = low + upp + special + nos


random_password = ""
for i in range(10):
    ran_letter = random.choice(str_all_letters)
    random_password += ran_letter

print("Your Random Password is:", random_password)