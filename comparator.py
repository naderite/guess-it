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


"""#TEST
user_input=input("try to guess the word: ")
genarated_number=["1","2","2","3","4","5","6"]

right,wrong,mis=compare(user_input,genarated_number)
print("rignt=",right,"wrong=",wrong,"mis=",mis)"""