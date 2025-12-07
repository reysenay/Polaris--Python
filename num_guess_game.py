import random

number_unknown= random.randint(1,10)

while True:
    try:
        number_guess= int(input("Enter your guess: "))

        if number_guess >number_unknown:
            print("Your guess is too high")

        elif number_guess < number_unknown:
            print("Your guess is too low ")

        else:
            print("Helal olsun, You guessed the number.")
            break
    except ValueError:
        print("Enter a valid number!")
  

    

    