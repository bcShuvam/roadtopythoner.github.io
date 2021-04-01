n = 18
guess = 0
print("Guess my age")

while guess < 9 :
    user_input = int(input())
    if user_input > n:
        guess = guess + 1
        print("You're age is greater than my age.\nNo. of guess =",guess,"\b/9")
        continue
    elif user_input < n:
        guess = guess + 1
        print("You're guess is smaller than my age.\nNo. of guess =",guess,"\b/9")
        continue
    elif user_input == n:
        print("\t\t\tCongratulations ! \n \b\t\tYou have guessed my age.\n\t\t\t   Game Over.")
        print("No. of guess you took =",guess)
        break
