from random import choice

keywords = open("magic.txt").read().splitlines()
solution = choice(keywords)
print(solution)