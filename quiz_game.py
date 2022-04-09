print("Welcome to the Quiz Game!")
player = input("Do you want to play: ")

try:
    if player.lower() != "yes":
            quit()
except:
    print("Goodbye!")
else:
    print("Let's play!")
    score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That answer is correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphical processing unit":
    print("That answer is correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for ").lower()
if answer == "random access memory":
    print("That answer is correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("That answer is correct!")
    score += 1
else:
    print("Incorrect")

print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/4) * 100) + "%")
