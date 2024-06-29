print("Welcome to my Computer Quiz Game.")

playing = input("Do you play this Game? ")

if playing.lower() != "yes":
    quit()

print("okay! let's paly :)")

score = 0

answer = input("what dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what dose GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what dose ROM stand for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what dose PSU stand for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print(f"you are correct {score} Question.")
print(f"you got {(score/4)*100}%")
