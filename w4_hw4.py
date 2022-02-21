import random
import time
guess = int(input("Enter an integer from 1 to 20: "))
guess_counter=1
#start time counter
start_time = time.perf_counter()
print("This time is being calculated")
n = random.randint(1, 20)
#print(n)
while n != "guess":

    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 20: "))
        guess_counter+=1

    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 20: "))
        guess_counter+=1

    else:
        print ("you guessed it!")
        break
        
print("Congratulations, you were right, the answer was {} ! It took you {} tries.".format(guess, guess_counter ))  
end_time = time.perf_counter()
e=int(end_time-start_time)
print("total guesses time :",'{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))