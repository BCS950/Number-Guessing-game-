import random 
number = random.randrange(1,200)
User = int(input("Guess 🧠 a number between 1 and 200: "))

if User == number:
  print(number)
  print("You guessed the number! 😮")

elif User > number:
  print (number)
  print("Your guess number is too high! 😞")
else:
 print (number)
 print("Your guess number is too low! 😞")
print = ("The number was", number)

