import random



robot_score = 0
player_score = 0


while True:
    num = random.randint(1,10)

    good_guess = False

    while not good_guess:
        try:
            guess = int(input('Guess a number between 1 and 10: '))    
            
            if guess < 1 or guess > 10:
                raise ValueError()

            good_guess = True
        except ValueError:
            print("Sorry I didnt understand that. Please try again.")
    
    times = 1

    while times < 3 and guess != num:
        if (guess > num):
            try:
                guess = int(input('Lower. Please guess again: '))
            except ValueError:
                print("Sorry I didnt understand that. Please guess again:")
                    
        else:
            try:
                guess = int(input('Higher. Guess again: '))
            except ValueError:
                print("Sorry I didnt understand that. Please guess again:")

        times = times + 1

        if (times == 3):
            print('Too many tries!')
            
            

    if (guess == num):
        player_score = player_score + 1        
        print('You win!', player_score, 'vs', robot_score, '\,,/(^_^)\,,/')

    else:
        robot_score = robot_score + 1        
        print('You lose! The number was ' + str(num) + '. ',player_score, ' vs ', robot_score, '¯\_(oO)_/¯',sep='')