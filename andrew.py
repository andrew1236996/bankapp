import random

top_of_range = input("type a number: ")

if top_of_range .isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
      print("please type a number larger than 0")
      quit()
else: 
    print("please type a number next time")
    quit()
    
random_number = random.randint(0,top_of_range)

while True:
    userguess = input("make a guess: ")
    if userguess.isdigit():
      userguess = int(userguess)

else:
    print("please type a number next time")
    

    if userguess == random_number:
     print("you got it")

    