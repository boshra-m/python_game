import time
import random


listOfReply = ['Enter 1 to go to the cave',
               'Enter 2 to go to the house']
listEnt1 = ['you reach a crosstoads, would you like to left or right? ',
            'There are wolfs, Enter: 2 to lgiht a fire or 3 to find another cave: ']
liseattach = ['you lost the game', 'take the hummer and fight']
ready = ['you are win', 'you are lost']


def play():
    while True:
        ans = input('would you like to play the game? (yes/no)')
        if ans.strip().lower() == 'yes':
            yes()
            break
        elif ans.strip().lower() == 'no':
            break


def yes():
    while True:

        print('Enter 1 to go to the cave')
        time.sleep(1)
        print('Enter 2 to go to the house')
        time.sleep(1)
        ansYesNo = input('Enter here:')
        if ansYesNo.lower().strip() == '1':
            time.sleep(1)
            y = input(random.choice(listEnt1))
            if y.lower().strip() == 'left':
                ann = input(
                    'you encounter a crocodile, would you like to attack or run?')
                if ann.lower().strip() == 'attack':
                    print('that was not the greatst idea, you lost')
                elif ann.lower().strip() == 'run':
                    time.sleep(1)
                    print('that is good choice')
                    time.sleep(1)
            elif y.lower().strip() == 'right':
                time.sleep(1)
                print(
                    'you walk without aim, and fall in ice lake and injured your leg, you can not continue. GAME OVER')
                time.sleep(1)
            elif y.lower().strip() == '2':
                time.sleep(1)
                print('Enter 1 to stay calm and have something to eat till the morning')
                time.sleep(1)
                print('Enter 2 to make the wolfs go away')
                time.sleep(1)
                n = input('Enter here :')
                if n.lower().strip() == '1':
                    time.sleep(1)
                    print('right call')
                elif n.lower().strip() == '2':
                    time.sleep(1)
                    print(
                        'very brave, but there are too many wolfs, they attacked you, and you are very injured, GAME OVER')
            elif y.lower().strip() == '3':
                time.sleep(1)
                print(
                    'right call, keep walling for three minutes there is a big cave next to the Lake')
            time.sleep(1)
            play()
        elif ansYesNo.lower().strip() == '2':
            time.sleep(2)
            attachORrun()
            break


def attachORrun():
    while True:
        ans = input('there is a monster in the house!! (attach/run)')
        if ans.strip().lower() == 'attach':
            time.sleep(2)
            res = 'take the hummer'
            finalStep()
            play()
        elif ans.strip().lower() == 'run':
            time.sleep(2)
            print('you take the safe dissection')
            play()


def finalStep():
    while True:
        ans = input(
            'when you ready go inside the house and Fighting.. (ready!?)')
        if ans.strip().lower() == 'ready':
            time.sleep(3)
            res = random.choice(ready)
            print(res)
            play()
            break


play()
