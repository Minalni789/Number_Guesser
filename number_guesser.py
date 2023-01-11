import random

top = input("Type a number larger than 0 to set top of the range: ")

if top.isdigit():
    top=int(top)

    if top <= 0:
        print("Try with a number larger than 0 next time")
        quit()
else:
    print("Please type a number")
    quit()

r = random.randint(0, top)

guesses = 0
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1

    else:
        print("Please type a number")
        continue

    if user_guess == r:
        print("You got it!")
        break
    else:
        print("You got it wrong")
        if user_guess > r:
            print("Try with a smaller number")
        else:
            print("Try with a larger number")


print(f"You got it in {guesses} guesses")
