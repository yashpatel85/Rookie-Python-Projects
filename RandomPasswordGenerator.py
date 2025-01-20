import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '&', '*']

ask_letters = int(input("How many letters do you want the password to consist of?: \n"))
ask_numbers = int(input("How many numbers do you want the password to consist of?: \n"))
ask_symbols = int(input("How many symbols do you want the password to consist of?: \n"))

#Easy Level

#password = ""

# for char in range(0,ask_letters):
#     password += random.choice(letters)
#
# for char in range(0, ask_numbers):
#     password += random.choice(numbers)
#
# for char in range(0, ask_symbols):
#     password += random.choice(symbols)
#
# print(password)

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#Hard Level
password_list = []

for char in range(0,ask_letters):
    password_list.append(random.choice(letters))

for char in range(0, ask_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, ask_symbols):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)


password = ""

for char in password_list:
    password += char

print(f"Your Password is: {password}")






































































