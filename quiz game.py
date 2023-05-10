print("Welcome To My Computer Quiz! " )
playing = input("do you want to play (yes/no): ").lower()
score=0
if playing != "yes":
    quit("thank you")
else:
    print("okay! let's play :) ")

answer=input("What does cpu stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does gpu stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does psu stands for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does rom stands for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " question Correct!")
print ("you got " +str((score/5)*100)+"%")

