print("Welcome to Treasure Island.")
print ("Your Mission is to find the treasure.")

decision = input("1. Left or right?: ")

if (decision == "right"):   print("Game Over.")

else: 
    
    decision = input("2. swim or wait?: ")

    if (decision == "swim"):    print("Game Over.") 
    else: 
        
        decision = input("3. Which door? Red, Blue or Yello?: ")
        
        if (decision == "yellow"):  print("You win!")
        else: print("Game Over.")

