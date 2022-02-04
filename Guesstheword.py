#imports
import random as rd


#constants and dictionaries
WELCOME="Welcome to my version of guess it! Thank you so much for trying it, and i hope you enjoy it\nWrite \"number\" or \"word\" to pick a game\ntype \"quit\" to quit the game"

WORDS_L=["impossible","part","music","bedroom","age","wheat"]
WORDS={
    "impossible":[
        "the first 2 letters verifies a word that means \"myself\""
                  ,"i am a 10 letter word","the last 8 letters verifies that you can complete it",
                  "the first 5 letters can be used for the word \"imposter\"","the last 3 letters can be used for the word \"bible\""],
    "music":[
        "My stem's planted firmly where I am allotted","My tail is wavy and my face is quite blotted.",
        "I relay much emotion though flatly I'm spotted, And I grow half my size whenever I'm dotted.",
        "I can speak any language, yet utter no words.","I'm no seed, yet I am well known among birds. But I do have a speech impediment: I can say cage but not page, aged but not wage."],
    "part":[
        "Another word for this word is fragment.","I am a 4 letter word.","The last 3 letters represent creativeness.",
        "If you change the first letter in this word into \"C\", the first three letters would be \"car.\"",
        "the first and the last letter are the abbreviation fo point"],
    "bedroom":[
        "I am the prefered place of lazy people","I am a 7 letter word.","The last 3 letters can be used for the letter, \"doom.\"",
        "The first 3 letters is the name of an object you need if you want to sleep confortably.",
        "The last 4 letters is a place in your house, maybe in a mall, etc"],  
    "age":[
        "I am something people love or hate","I change peoples appearances and thoughts.",
        "If a person takes care of them self I will go up even higher.","To some people I will fool them. To others I am a mystery.",
        "Some people might want to try and hide me but I will show.","No matter how hard people try I will Never go down."],
    "wheat":["this plant is a 5 letter word","if you take away first letter it is something you get from sun",
             "if you remove second letter you will get something to eat","if you remove third letter you get a word you use in pointing at",
             "and if you remove the fourth letter you get something to drink"]     
}

PLAYING=True

#comparator
def compare(guess,answer):
    #lists of the results of the comparison

    right=[]
    misposioned=[]
    wrong=[]
    
    for pos in range(0,len(guess)):
        
        if guess[pos] in answer:#check if the letter in the Genarated word
            
            try:
                if guess[pos]==answer[pos]:#check if the letter in the right place
                    right.append(guess[pos])
            
                else:     
                    misposioned.append(guess[pos])
            
            except IndexError:#works if the letter exist but the position is higher than ANSWER lenth  
                misposioned.append(guess[pos])
                
            #if the number of the right/mispositioned is higher than ANSWER moves them to wrong    
            if misposioned.count(guess[pos])+right.count(guess[pos])>answer.count(guess[pos]): 
                misposioned.remove(guess[pos])
                wrong.append(guess[pos])
                
                
        else:#store the wrong letters
            wrong.append(guess[pos])
     
                   
    return right,wrong,misposioned

#number genarator
def genarate(lenth):
    genarated=""
    for number in range(0,lenth):
        genarated=genarated+(str(rd.randint(0,9)))
      
    return genarated

#message writer
def write(right,wrong,missed,lifes):
    print("\nthe correct numbers are:",str(right),"\nthe misplaced numbers are:",str(missed),"\nthe wrong numbers are:",str(wrong),"\nthe remaining lifes:",str(lifes))
    
#Win or lose checker
def check(guess,correct,lives):
    win= False
    lose=False
    if guess==correct:
        win=True
    elif lives==0:
        lose=True
    return win,lose



#main loop
print(WELCOME)
while PLAYING:
    LIVES=5
    win = False
    lose=False
    
    #choosing the game mode
    choice=input("Game mode:")
    if choice=="quit":#checks if the user wanna quit
        break 
    
    while not(choice in["number","word"]):
        choice=input("You typed it wrong try again\nGame mode:")
        if choice=="quit":#checks if the user wanna quit
            PLAYING=False
            break
        
    
    #Guess the number mode
    if choice == "number":
        
        print("\nI am thinking of a 6 digits number you need to guess it to win\nyou have ",LIVES,"lifes\n think before you try")
        
        number=genarate(6) 
        
        while not(win or lose):
            
            guess=input("\ntry to guess the number: ")
            
            if guess=="quit":#checks if the user wanna quit
                PLAYING=False
                break
            
            LIVES-=1
            right,wrong,mis=compare(guess,number)
            win,lose=check(guess,number,LIVES)
            write(right,wrong,mis,LIVES)
            
    #Guess the word mode
    if choice == "word":
        print("\nI am thinking of a word you need to guess it to win\nyou have ",LIVES,"lifes\n think before you try")
        
        word=rd.choice(WORDS_L)
        hints=WORDS[word]
        num=0
        while not(win or lose):
            #give a hint
            print(hints[num])
            num+=1
            guess=input("\ntry to guess it: ")
            
            if guess=="quit":#checks if the user wanna quit
                PLAYING=False
                break
            
            LIVES-=1
            right,wrong,mis=compare(guess,word)
            win,lose=check(guess,word,LIVES)
            write(right,wrong,mis,LIVES)    
    
    
    #win/lose message
    if win:
        print("\nCongrats!\nif you want to play again pick a game user\nif you want to quit type\"quit\"")
    elif lose:
        print("\nOOPS! you lost!\nif you want to play again pick a game user\nif you want to quit type\"quit\"")








