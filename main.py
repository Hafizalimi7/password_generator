#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

password_list = []

nr_letters= (input("How many letters would you like in your password?\n")) 
for i in range(0,int(nr_letters)):
  len_let = len(nr_letters)
  password_list += letters[random.randint(0,len_let)-1]
  
nr_symbols = (input(f"How many symbols would you like?\n"))
for j in range(0,int(nr_symbols)):
  len_sym = len(nr_symbols)
  password_list += symbols[random.randint(0,len_sym)-1]

nr_numbers = (input(f"How many numbers would you like?\n"))
for k in range(0,int(nr_numbers)):
  len_num = len(nr_numbers)
  password_list += numbers[random.randint(0,len_num)-1]
random.shuffle(password_list)
password = ''.join(password_list)
print(f'this is your password, {password}')

 

