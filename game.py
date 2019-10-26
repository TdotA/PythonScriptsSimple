import random

number = random.randint(1,100)
lives = 7
user = int(input('Enter your number: '))

while user!=number and lives > 1 :
    if user < number:
        print ('Think bigger')
    else:
        print('Too fucking big you stupid fuck')
    user = int(input('Enter your number: '))
    lives -= 1

if user == number :
    print('You are correct')
elif lives == 1 :
    print('Number was: ' + str(number))