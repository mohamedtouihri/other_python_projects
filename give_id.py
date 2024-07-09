is_tunisian = input("Are you tunisian? Type 'yes' or 'no'").lower()
if is_tunisian == "yes":
  print("Good, that's the first step")
  is_18 = input("Are you above 18? Type 'yes' or 'no'").lower()
  if is_18 == "yes":
    print("You can have and ID")
  else:
    print("Sorry, you have to be 18 or older \nPlease try again when you are 18")
else:
  print("Sorry ,an tunisian ID is give only to Tunisians")














