#Welcome
print("Welcome to my computer quiz!")  

playing= input("Do you want to play my quiz? ")

#Declaration 
score= 0 

if playing.lower()!= "yes":
   quit()
else: 
   print("Okay! Let's play the game:) ")

#Que1
answer=  input("What does CPU stand for? ")
if answer.lower()!= "central processing unit":
   print("Incorrect! ")
else: 
   print("Correct! ")
   score+=1

#Que2
answer=  input("What does GPU stand for? ")
if answer.lower()!= "graphics processing unit":
   print("Incorrect! ")
else: 
   print("Correct! ")
   score+=1

#Que3   
answer=  input("What does RAM stand for? ")
if answer.lower()!= "random access memory":
   print("Incorrect! ")
else: 
   print("Correct! ")
   score+=1

#Que4  
answer=  input("What does PSU stand for? ")
if answer.lower()!= "power supply":
   print("Incorrect! ")
else: 
   print("Correct! ")
   score+=1

#Output
print("You got " + str(score) + " questions right.")
print("You got " + str(score/4 * 100) + "%.")
   
