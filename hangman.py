import random
from collections import Counter
#random library is used to take random word
#Counter is used to check number of times the alphabet is used in the word

all_players= "Michael, Pele, Serena, Usain, Muhammad, Roger, Lionel, Jackie, Michael, Marta, Wayne, Jerry,  Sachin, Ronaldo"
word = random.choice(all_players.split(', ')).lower()
#this will select a random word from above

chances = len(word)+3
letter_guessed = ''
count = 0
flag = 0
#above variables are used to store the guessed letter, to check number of chances and if game has ended

print('Welcome to the word guessing game!!!!!!')
print('Hint!!! It\'s a sports person name')

for i in word:
    print('_', end=' ')
# will print'_' for each letter in the word
try:
    while count < chances:
        count += 1

        try:
            choice = str(input('Please guess a letter : ')).lower()
        except:
            print('Please enter an alphabet.')
            continue

#Below is for the validation of the  guess.
        if not choice.isalpha():
            print('Please only enter an alphabet. ')
            continue
        elif choice in letter_guessed:
            print('You have already guessed the letter. ')
            continue
        elif len(choice) > 1:
            print('Please enter only one alphabet. ')
            continue

#What will happen if letter was guessed correctly
        if choice in word:
            k= word.count(choice)
            for _ in range(k):
                letter_guessed += choice #storing the correct letter same number of time  in the word

        for char in word:
            if char in letter_guessed and (Counter(word) != Counter(letter_guessed)):
                print(char, end=' ')
                #count -= 1
            elif Counter(word) == Counter(letter_guessed):
                print('Congratulations you Won the game')
                print(f'The word is {word}')
                flag += 1
                break               
            else:
                print('_', end=' ')
        if flag  == 1:
            break

    if count == chances:
        print('You lost the game!!! \n No more chances left')
        print(f'The word was {word}')
except KeyboardInterrupt:
    print('Game interrupted !! Visit agin for the fun')
    exit()

