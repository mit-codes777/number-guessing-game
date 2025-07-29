print(" Welcome to number guessing game ")
import random
com = random.randint(1,100)

count = 0 
while True:
    user = input("Enter a guessing number : ")

    if not user.isdigit():
        print("Please enter numbers only")
        continue

    guess = int(user)    
    count += 1
    
    if guess < com:
        print("Guess higher ")
    elif guess > com:
        print("Guess lower")
    else:
        print("Congratulations, You guessed correctly")
        print(f"You guess in {count} attempts")
        break