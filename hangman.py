import random 
 
words = ["spooky", "halloween","pumpkin"] 
#we can have multiple lists 
#with various difficulty levels 
target = random.choice(words) 
print(target) 
 
progress = ['_'] * len(target) 
print(*progress) 
lives = 6 
running = True 
while running: 
    guess = input("Enter a character: ") 
    #validate guess (single character) 
    if len(guess) != 1: 
        print("Please enter a single character.") 
        continue 
 
    if guess not in target: 
        print("Wrong guess!") 
        #check if the user has lost the game 
        lives = lives - 1 
        print("Lives left:", lives) 
        if lives == 0: 
            print("You lost!") 
            running = False 
    else: 
        for i in range(len(target)): 
            if target[i] == guess: 
                progress[i] = guess 
        #check if the user has won the game 
        if '_' not in progress: 
            print("You won!") 
            running = False 
    print(*progress)
