"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main(N_TURNS):
    """
    Pre-condition: The user sees a dashed word and try inputting one character each round
    Post-condition: If the input is correct, updated word will replace the dashed word; if not, the program will print the times of wrong guess left; or the illegal format 
    """
    # begin: 把Randon的長度輸出成字串k,
    # guess: 接收的字母key，把跟key相同的-取代為key，輸出新字串ans


    Ran=random_word().upper()
    k=begin(Ran) # 一開始呈現的字串有k個-，k為字串------...共k個'-'
    print('The word look like ', k)

    while True:
        key = input('Your guess: ').upper()
        if key.isalpha():
            if key in Ran: # 有猜中的情況
                k=guess(k, Ran, key) # k被換成新的字串
                if k.find('-') == -1: # 若k已經沒有'-'代表全猜到了
                    print('You are correct!\nYou win!\nThe word was: ', k)
                    break
                else:
                    print('You are correct!\nThe word look like ', k,'\nYou have ', N_TURNS, 'wrong guess left.')
            else: # 沒猜中的情況
                print('There in no', key, 'in the word.\nThe word look like ', k)
                N_TURNS-=1
                print('You have ', N_TURNS, 'wrong guess left.')
                if N_TURNS==0:
                    print('You are completely hung ：（\nThe word was: ', Ran)
                    break
        else: # 若輸入不是字母的情況
            print('illegal format.')


def begin(Ran):
    """
    Pre-condition:The function received the random word Ran
    Post-condition:The function will return '-' with length same as the word Ran
    """
    a=''
    for i in Ran:
        a+='-'
    return a


def guess(k,Ran,key): # 輸入舊字串k, 被猜的字Ran, 使用者輸入的字母key
    """
    Pre-condition: The function receive old string 'k', random word 'Ran' and guessed word 'key'
    Post-condition: The function will return new string 'ans' according to guessed word 'key'
    """
    ans=''
    for i in range (len(k)):
        if Ran[i]==key:
            a=key
        else:
            a=k[i]
        ans+=a
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main(N_TURNS)
