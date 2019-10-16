import random


times = 1
robot_score = 0
player_score = 0


while True:
    num = random.randint(1,10)
    try:
        guess = int(input('Guess a number between 1 and 10: '))    
    except ValueError:
        guess = int(input("Sorry I didnt understand that. Please guess again: "))
            

    while guess != num:
        if (guess > 10):
            print('The number must be between 1 and 10')
            times = times -1
            

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
            break
            print('You lose! The number was ' + str(num))
            

    if (guess == num):
        player_score = player_score + 1        
        print('You win!', player_score, 'vs', robot_score, '\,,/(^_^)\,,/')

    else:
        robot_score = robot_score + 1        
        print('You lose! The number was ' + str(num) + '. ',player_score, ' vs ', robot_score, '¯\_(oO)_/¯',sep='')