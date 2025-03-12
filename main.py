# Nathan Saez
# Carter Traveller
# Spencer Ord
from character import Character


# Initial welcoming to the game. Here the game will be explained and they will create their character
name = input('Welcome to the Hack Your Own Adventure Game! Please enter your first name: ')
print(f'\nHello, {name}, and welcome! In this game you will be faced with many decisions.')
print(f'Some of the decisions you make will affect what happens later on, so be smart.')
print('In this game, you will take on the role of a person who wants to attack a company.')
print('Before we continue, we will need some basic information.')

age = input('Please enter your age: ')
gender = input('Please enter your gender(M/F): ')

attacker = Character(name, age, gender)

print(f"\nAlright {attacker.name}, we are ready to go! Now its time to start your adventure!\n")

