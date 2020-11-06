import random


WORDS = ("SLAVES","FUCK","order","this","shit")

i = 0
u = []
used = []


print("welcome")
input("Нажмите кнопку для продолжения")
while i < len(WORDS):
    lent = len(WORDS) - 1
    rand = random.randint(0, lent)
    if rand not in u:
        print(WORDS[rand])
        used.append(WORDS[rand])
        u.append(rand)
        i = i + 1
    else:
        continue

