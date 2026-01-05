import random

number = random.randint(1, 100)
attempts = 0

print("Devinez un nombre entre 1 et 100")

while True:
    guess = int(input("Votre choix : "))
    attempts += 1

    if guess < number:
        print("Trop petit")
    elif guess > number:
        print("Trop grand")
    else:
        print("Bravo ! Trouvé en", attempts, "essais")
        break
