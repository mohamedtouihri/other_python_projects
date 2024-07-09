import random
pin = int(input("Enter a 4-digit PIN code: \n"))
code = random.randint(1000,9999)
if len(str(pin)) != 4 :
 print("Please Enter 4 digits")
elif pin == code :
  print ("Good, Your PIN is correct")
else:
  print("Failed! PIN code did not match.")
  print(f"The Computer generated this PIN: {code}")