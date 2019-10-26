lives = 7
user = int(input('Enter your guess you svine: '))
left = 1
right = 100
while right != left :
    if user < left or user > right:
        print('Are you retarted')
        user = int(input('Guess again: '))
    else :
        while (right != left) and lives > 1 :
            if right - user >= user - left :
                left = user + 1
            else :
                right = user - 1
            print('Number is between: ' + str(left) + ' and ' + str(right)) 
            user = int(input('Enter your guess you svine: '))
print ('number is ' + str(user))