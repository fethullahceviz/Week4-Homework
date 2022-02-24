import random
import time
a,b=int(input("Set a range for the guessing game R1: ")),int(input("Set a range for the guessing game R2: "))
guess = int(input("Enter an integer from " + f"{a} "+"to "+ f"{b}: "  ))
guess_counter=1
#start time counter
start_time = time.perf_counter()
print("This time is being calculated")
n = random.randint(a, b)
#print(n)
while n != "guess":

    if guess < n:
        print ("Guess is low  ")
        guess = int(input("Enter an integer from " + f"{a} "+"to "+ f"{b}: "  ))
        guess_counter+=1

    elif guess > n:
        print ("Guess is high ")
        guess = int(input("Enter an integer from " + f"{a} "+"to "+ f"{b}: "  ))
        guess_counter+=1

    else:
        print ("You guessed it!")        
        break
        
end_time = time.perf_counter()
e=int(end_time-start_time)
print("Congratulations you were right the answer was",f"{guess}")
print("TotalNumberofTries :",f"{guess_counter}")
print("TotalGuessesTime   :",'{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))