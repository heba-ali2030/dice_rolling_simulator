import random
# 1- check validity of game settings:
def settings_validity(game_settings):
    list =['d', 's' ]
    while game_settings not in list:
        print(' please check your typing, only d or s letters is acceptable to play!')
        game_settings = input('Type d for default or s for self settings:\n ').casefold()

    return game_settings

# 2- check validity of rolling again input:
def spelling_validity(play_again):
    list =['y', 'yes' , 'no', 'n']
    while play_again not in list:
        print(' ooh, sorry, I don\'t understand your choice!')
        play_again = input('Type Yes or y to play again and no or n to exit ! \n ').casefold()

    return play_again

# 3- check numbers
def number_validity(number):
    while number.isdigit == False:
        number = input('please enter only integer number to continue: ')
    return int(number)

# function to evaluate your luck in rolling dice


# greetings and begin the game:
print(f'Hi, let\'s play together!\n')

#ask the user to choose either default setting or self setting:
print(f'Please, choose default or self settings to play :\n Remember:\n << default >> is rolling dice between average of 1 and 6 >>>.\n, While in << self setting >> you can choose your range')

game_settings = settings_validity(input('Type d for default or s for self settings:\n ')).casefold()

run = 0
while True:
    # if choice is default settings:
    if game_settings == 'd'.casefold():
    # make random choice between (1) and (6)
        dice = random.randint(1, 6)

    # if the choice is self settings:
    else:
        # ask the user to choose minimum (min) number for the dice
        minimum = number_validity(input('please type the minimum number you want: \n'))
        # ask the user to choose maximum (max) number for the dice
        maximum = number_validity(input('please type the maximum number you want: \n'))
        # make random choice between (min) and (max)
        dice = random.randint(minimum, maximum)

    # print the user rolling number
    def luck():    
        if dice == max or dice == 6:
            print(f'wooooow, your dice number is {dice} ')
        else:
            print(f'Not bad, your dice number is {dice}')
        
    luck()
    print('----------------------------------------------------------------------')

    # Ask the user to roll dice again or to exit
    play_again = spelling_validity(input('Do you want to roll again? \n Type Yes or y to play again and no or n to exit ! \n ')).casefold()

    # if choose yes:
    if play_again == 'n' or play_again == 'no':
        print('Waiting to see you again ^_^')
        break
    
 # to leaave space between rolling:
    print('^_^')

