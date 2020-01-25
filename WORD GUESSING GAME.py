#this is simplest  version if word guessing game 
# happy playing
#plese report if you find any  buggy thing in it .. at Email: rr200636@gmail.com
#code written by rahul raikwar
import random
list1= ["dog","cat","mango","pen","copy","bike","marker"]
list2=[ ]

#randon is use to take a random word from list
print("\nWELCOMING TO THE WORD GUESSING GAME \n **** - wanna play  - ***\n let's start")

random_word = random.choice(list1)
print("\nLET ME GUESS A WORD")

#this loop is appned the underscore *length so we can ittrate over it
for i in range(len(random_word)):
    list2.append(" _ ")

#starting loop to get the input from user
print("\n\t$ -Guess any  'LETTER' of the word to start -$\n")
while True:
    list3 = [i for i in random_word]
    user_input = input().lower()
    
    #to check weither the usr input is in the guessed word or not
    if user_input in random_word:
        word_index= list3.index(user_input)
    
        list2[word_index] = user_input
        b = " ".join(list2)    
        print(f"\n{b}")
        
        #if player guessed all blanks it must be equle list
        if list2==list3:           
            print("\n------**** ---congratulation -----****\n")
            break
        else:
            print("\n**** next word plss ***\n")
            continue
    else:
        # this for exception handling
        print("\n ops..! WRONG INPUT****")