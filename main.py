#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("\n")
random_letters = random.choices(letters, weights=None, cum_weights=None, k= nr_letters)
random_letters_str = ''.join(random_letters)
print(random_letters_str)
random_symbols = random.choices(symbols, weights=None, cum_weights=None, k= nr_symbols)
random_symbols_str = ''.join(random_symbols)
print(random_symbols_str)
random_numbers = random.choices(numbers, weights=None, cum_weights=None, k= nr_numbers)
random_numbers_str = ''.join(random_numbers)
print(random_numbers_str)
#print (f"Your password is {random_letters_str}{random_symbols_str}{random_numbers_str}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
combine_list = random_letters + random_numbers + random_symbols
random.shuffle(combine_list)
combine_list_str =''.join(combine_list)
print(f"Your password is {combine_list_str}.")

#--- solution ---
#Easy Level
# password = ""

# for char in range(1,nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1,nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1,nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

##Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

## following code Turning password_list into a string
# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")