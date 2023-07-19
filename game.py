from random import shuffle

#Shuffling the Ball
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    
# result = shuffle_list(mylist)
# print(result)

def players_guess():
    
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number :0 ,1 or 2 ") #input alwys return string
        
    return int(guess)
    

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)
        


#INITIAL LIST
mylist = ['','O','']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = players_guess()

#CHECK GUESS

check_guess(mixedup_list,guess)