import random

magic_number = random.randint(1,10)
print("Welcome to the Million dollar game, you will have 2 opportunities to try, think carefully")
counter = 1
previous_guesses = []

print(5)

while counter < 3:
  print("YOu have previously guessed:")
  print(previous_guesses)
  user_guess = int(input("Guess a number between 1 and 10: "))
  previous_guesses.append(user_guess)

  if user_guess == magic_number:
    print("You won!")
    break
  else:
    print("Your guess was incorrect.")

  counter = counter + 1

if counter == 0:
  print("You lose!")
