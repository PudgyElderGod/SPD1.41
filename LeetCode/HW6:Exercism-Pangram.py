#Problem: Determine if a sentence is a pangram in the English language.
#Pangrams are sentences that use every letter of an alphabet. 


#Q: Is it case sensitive?
#A: It is not case sensitive

def panagram(sentence):
    count = {}
    for letter in sentence:
        l = letter.lower()  #convert to lowercase
        #check to see if character is a letter
        if l.isalpha():     
            #adds it to the count if it is a letter
            if count.get(l) == None:
                count[l] = 0
            else:
                count[l]+=1
    #check to see if the length of count is 26
    if len(count) == 26:
        return True
    else: 
        return False

assert panagram("The five boxing wizards jump quickly.") == True
assert panagram("She sells sea shells by the sea shore") == False