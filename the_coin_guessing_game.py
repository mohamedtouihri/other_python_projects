import random
print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")
method = int(input("Enter your choise (1 or 2) "))
if method == 1:
  choisee = input("Enter your Guess (Heads or Tails): ").lower()
  random_choise = random.random()
  if random_choise <= 0.5:
    computer_result = "heads"
    if computer_result == choisee:
      print("Congratulations! You won!")
      print("The computer's coin toss result was : "+ computer_result)
    else:
      print("Sorry you lost!")
      print("The computer's coin toss result was : "+ computer_result)
  else:
    computer_result ="tails"
    if computer_result == choisee:
      print("Congratulations! You won!")
      print("The computer's coin toss result was : "+ computer_result)
    else:
      print("Sorry you lost!")
      print("The computer's coin toss result was : "+ computer_result)  
elif method == 2:
  choise = input("Enter your Guess (Heads or Tails): ").lower()
  randint_choise = random.randint(0,1)
  if randint_choise == 0:
   computer_result = "heads"
   if computer_result == choise:
      print("Congratulations! You won!")
      print("The computer's coin toss result was : "+computer_result)
   else:
      print("Sorry you lost!")
      print("The computer's coin toss result was : "+ computer_result)
  else:
    computer_result ="tails"
    if computer_result == choise:
      print("Congratulations! You won!")
      print("The computer's coin toss result was : "+ computer_result)
    else:
      print("Sorry you lost!")
      print("The computer's coin toss result was : "+ computer_result)  
else:
  print("Invalid choise. Please select either 1 or 2")
