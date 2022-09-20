#
#colby B Apichell
#
#
#09/20/2022
#
#this is a test lab using loops to make a text base game
#resource used below
#https://www.youtube.com/watch?v=u8X6TiJA8as
#
#


name = input('Enter your name ')
age = input('Enter your age!')
print(f'greetings {name} or {age} years around the yellow guardian! Welcome to you adventure!')
start = input('Would you rather play this gamne or die? (play/die)')
if start == 'play':
    print('Great, lets play the game!')
    setting = input('Want to go the jungle temple or the desert temple to choose your deity? (jungle/desert)')
else:
    print('Lame, okay you fall over and die of heart attack. (Ending 1 of 6 found!)')
    quit()

if setting == 'jungle':
    print('You arrive at the mighty jungle, with steamy rays of sunshine peeking through the leaves. You are told to wait while the elders are summoned.')
    response = input('But you have waited long and grow impatient. Thrits and hunger pang you greatly. (Follow) to the village, or (wait here)?')
    if response == 'follow':
        print('You follow the guide to the village.')
# this where you nest another variable in this case transport
        transport = input('You see a horse that is frail and an old cart, do you (ride) the hoirse and cart or (walk)?')
        if transport == 'ride':
            print('You mount the horse in one fell swoop. It collpases beneath you and dies. Now someone will surely be mad at you.')
        elif transport == 'walk':
            print('You begin down the path, dust caking your nostrils and stinging sweat dripping into your eyes. It is agony.')
        else:
            ('You doze off and are eaten by a pack of wild animals! Ending 3 of 6 found!')
            
    elif response == 'wait here':
        print('You wait another ten minutes, youi hunger gnawing and thirst are beckoning!')
    else:
        print('You doze off and are eaten by lions! Ending 2 of 6 found!')
        quit()


elif setting == 'desert':
    print('You arrive at the dry and windy dunes, with hot rays of sunshine smashing down. You are told to wait while the elders are summoned.')
    response = input('But you have waited long and grow impatient. Thirst and hunger pang you greatly. (Follow) to the village, or (wait here)?')
    if response == 'follow':
        print('You follow the guide to the village.')
    elif response == 'wait here':
        print('You wait another ten minutes, you hunger gnawing and thirst are beckoning!')
    else:
        print('You doze off and are eaten by lions! Ending 2 of 6 found!')
        quit()

