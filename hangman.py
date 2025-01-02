from random import choice

def get_guess():
    global progress
    guess = input("What's the letter\n\n").lower()
    if len(guess) == 1 and guess.isalpha():
        return guess
    elif guess == solution:
        progress = solution
        return guess
    print("no!")
    display_status()
    return get_guess()

def display_status():
    print(f"Guess {len(wrong) + 1}/6")
    print()
    print(''.join(progress))
    stop_the_count = ', '.join(sorted(wrong)) if len(wrong) else "none"
    print(f"wrong guesses used: {stop_the_count}\n")

def is_correct():
    return ''.join(progress).replace(" ", "") == solution

def update_progress(guess):
    if guess not in solution:
        wrong.add(guess)
    for (i, letter) in enumerate(solution):
        if letter == guess:
            progress[i] = letter + " "

keywords = open(r"C:\Users\Wassa\Desktop\python\hangman\magic.txt").read().splitlines()
solution = choice(keywords)
progress = ["_ "] * len(solution)
wrong = set()

while not is_correct() and len(wrong) < 6:
    display_status()
    update_progress(get_guess())
    
print(''.join(progress))
print("Yay!" if len(wrong) < 6 else f"Boo!\nAnswer was: {solution}")