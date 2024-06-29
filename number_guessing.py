import random

top_of_range = input("Enter the number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type number lager than 0 next time.")
        quit()
else:
    print("please must type numbers only.")
    quit()



random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_number = input("Gussing number : ")
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("please must type numbers only.")
        continue

    if user_number == random_number:
        print("you got it")
        break
    elif user_number > random_number:
        print("your guessing number is above random number")
    else:
        print("your guessing number is belove random number")

print(f"your guessing count : {guesses}")