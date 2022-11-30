import random

def check_answer(guess, answer):
    if guess > answer:
        return "Too High"
    elif guess < answer:
        return "Too Low"
    else:
        return f"You got it! The answer is {answer}"

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficult = input("Choose a difficult. Type 'easy' or 'hard'")

if difficult == 'easy':
    attemps = 10
else:
    attemps = 5

guess = 0

while guess != number and attemps:
    print(f"You have {attemps} remaining")
    guess = int(input("Make a guess:"))
    print(check_answer(guess, number))
    attemps -= 1
    if attemps == 0:
        print("No more chances you lose")