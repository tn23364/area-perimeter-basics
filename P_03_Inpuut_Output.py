# ask the user for their name
username = input('What is your name? ')

# ask the user for their favourite number (integer)
fav_num = int(input('What is your favourite number? '))

# double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# greet the user
print(f"\nHi {username}, your favourite number is {fav_num}")

# output the results of doubling, halving
# squaring their favourite number
print(f'Double {fav_num} is {double}.')
print(f'half {fav_num} is {halve}.')
print(f'{fav_num} squared is {square}')
print()
print('Have a nice day.')
