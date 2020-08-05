import time
import random


listOfReply = ['Enter 1 to go to the cave',
               'Enter 2 to go to the house']
listEnt1 = ['SAFE, you can stay here until the Morning', 'WOLFS, you lost']
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
            print(random.choice(listEnt1))
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
