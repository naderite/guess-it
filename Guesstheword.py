# imports
import random as rd


#constants and dictionaries
WELCOME_MESSAGE = "Welcome to my version of guess the word/number! Thank you so much for trying it, and i hope you enjoy it.","\nWrite \"number\" or \"word\" to pick a game.","\ntype \"quit\" to quit the game."

WORDS_LIST = ["impossible", "part", "music", "bedroom", "age", "wheat"]
WORDS_DICTIONARY = {
    "impossible": [
        "the first 2 letters verifies a word that means \"myself\"", "i am a 10 letter word", "the last 8 letters verifies that you can complete it",
        "the first 5 letters can be used for the word \"imposter\"", "the last 3 letters can be used for the word \"bible\""],
    "music": [
        "My stem's planted firmly where I am allotted", "My tail is wavy and my face is quite blotted.",
        "I relay much emotion though flatly I'm spotted, And I grow half my size whenever I'm dotted.",
        "I can speak any language, yet utter no words.", "I'm no seed, yet I am well known among birds. But I do have a speech impediment: I can say cage but not page, aged but not wage."],
    "part": [
        "Another word for this word is fragment.", "I am a 4 letter word.", "The last 3 letters represent creativeness.",
        "If you change the first letter in this word into \"C\", the first three letters would be \"car.\"",
        "the first and the last letter are the abbreviation fo point"],
    "bedroom": [
        "I am the prefered place of lazy people", "I am a 7 letter word.", "The last 3 letters can be used for the letter, \"doom.\"",
        "The first 3 letters is the name of an object you need if you want to sleep confortably.",
        "The last 4 letters is a place in your house, maybe in a mall, etc"],
    "age": [
        "I am something people love or hate", "I change peoples appearances and thoughts.",
        "If a person takes care of them self I will go up even higher.", "To some people I will fool them. To others I am a mystery.",
        "Some people might want to try and hide me but I will show.", "No matter how hard people try I will Never go down."],
    "wheat": ["this plant is a 5 letter word", "if you take away first letter it is something you get from sun",
              "if you remove second letter you will get something to eat", "if you remove third letter you get a word you use in pointing at",
              "and if you remove the fourth letter you get something to drink"]
}


def compare(guess, answer):

    right = []
    misposioned = []
   
    for letter in answer:
        #checks the letter is in the right place
        if answer.index(letter) == guess.index(letter):  
            right.append(letter)
        #checks if the letter is in the guess but misplaced
        elif guess.index(letter) not in [answer.index(letter),-1]:
            misposioned.append(letter)
        guess=guess.replace(letter,"")
    wrong=list(guess)

    return right, wrong, misposioned


def guess_the_word(lives):
    print("\nI am thinking of a word you need to guess it to win","\nYou have ",lives," lives","\n think before you try")
    word = rd.choice(WORDS_LIST)
    hints = WORDS_DICTIONARY[word]
    index = 0
    win= False

    while not(win) and lives>0:
        # give a hint
        print(hints[index])
        index += 1
        guess = input("\ntry to guess it: ")
        lives -= 1
        right, wrong, misposioned = compare(guess, word)
        win = guess == word
        print("\nthe correct numbers are:", right, "\nthe misplaced numbers are:", misposioned, "\nthe wrong numbers are:", wrong, "\nthe remaining lifes:", lives)
    return win,word

def guess_the_number(lives):
    print("\nI am thinking of a 4 digits number you need to guess it to win.\nYou have", lives," lives\nthink before you try")
    number = str(rd.randint(1000,9999))
    win=False
    while not(win) and lives>0:
        guess = input("\nTry to guess the number: ")
        lives -= 1
        right, wrong, misposioned = compare(guess, number)
        win = guess == number
        print("\nthe correct numbers are:", right, "\nthe misplaced numbers are:", misposioned, "\nthe wrong numbers are:", wrong, "\nthe remaining lifes:", lives)
    return win,number
    

print(WELCOME_MESSAGE)
# main loop
def main():
    playing = True
    lives = 5
    win = False
    answer = ""

    while playing:
        # choosing the game mode
        choice = input("Game mode:")
        # checks if the user wanna quit
        if choice == "quit": 
            playing = False

        while choice not in ["number", "word"]:
            choice = input("You typed it wrong try again.","\nGame mode:")
            # checks if the user wanna quit
            if choice == "quit": 
                playing = False
                break

        # Guess the number mode
        if choice == "number":
            win, answer=guess_the_number(lives)

        # Guess the word mode
        if choice == "word":
            win,answer = guess_the_word(lives)

        # final message message
        if win:
            print("\nCongrats!\nif you want to play again pick a game mode\nif you want to quit type\"quit\"")
        else:
            print("\nOOPS! you lost!","the right answer is:",answer,"\nif you want to play again pick a game mode:\nif you want to quit type\"quit\"")

if  __name__ == "__main__":
    main()