import random

current_word = random.choice(["toast", "abuse", "glove", "obese", "whole"])

#game loop
for i in range (5):
    guess = input(" ")
    for g in range(min(len(guess), len(current_word))):
        if guess[g] == current_word[g]:
            print(f"\033[32m{guess[g]}\033[0m", end="")
        elif guess[g] in current_word:
            print(f"\033[33m{guess[g]}\033[0m", end="")
        else:
            print(f"\033[31m{guess[g]}\033[0m", end="")
        
        print()
    if guess == current_word:
        print("congratulations")
        break;
    else:
        i-=1

