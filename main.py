# These are our functions
import random
from  adventureFunctions import *
# 
#animal guides - donkey, fish in a fishbowl, dog 
#
# the character selection should have some form of function or definition attatched to it that would have some impact to the role playing sence. IE the warior uses his great sword to open the door or the rouge would use his skills to open the locked door
print("help me")
# Ev code
yn = "n"
print()

print()

print()
print ("test")

print()

print()

print()
while yn == "n" or yn == "N":
  print ("Helo odd little traveler. you are about to embark on a perilous adventure in which you will choose your destiny. First.... Who are you")
  print()
  print ("A - The Mighty Warrior: A towering figure with rippling muscles, the mighty warrior wields a massive sword and wears armor adorned with intricate designs. Though fearsome in battle, this warrior is guided by a strong sense of honor.")
  print()
  print ("B - The Mysterious Mage: Cloaked in a billowing robe, the mysterious mage possesses an otherworldly aura and an arsenal of powerful spells. They keep to themselves, but when they speak, their words are filled with ancient wisdom.")
  print()
  print ("C - The Cunning Rogue: Quick-witted and nimble, the cunning rogue moves through the shadows like a whisper. They are experts at lockpicking and sleight of hand, and always have a trick up their sleeve.")
  
  print()
  print ("D - The Wise Elder: With a long white beard and piercing eyes, the wise elder is a font of knowledge and guidance. They have seen much in their long life and have many stories to tell. Though frail in body, their mind is sharp and their spirit unbroken.")
  print()
  print ("E - Dylan the bard: A wiley and charasmatic character that has been baned from more establishments than he patroned. His prowess with alcohol is matched only by his skill with maracas. He has no concept of personal space, boundries or, taste.")
  print ("Make your choice")
  choice = input()
  print()
  if choice == "A" or choice == "a":
      print ("A - The Mighty Warrior: A towering figure with rippling muscles, the mighty warrior wields a massive sword and wears armor adorned with intricate designs. Though fearsome in battle, this warrior is guided by a strong sense of honor. Is this your choice traveler? \nAre you certain")
  elif choice == "B" or choice == "b":
    print ("B - The Mysterious Mage: Cloaked in a billowing robe, the mysterious mage possesses an otherworldly aura and an arsenal of powerful spells. They keep to themselves, but when they speak, their words are filled with ancient wisdom. \nAre you certain")
    print ()
  elif choice == "C" or choice == "c":
      print ("C - The Cunning Rogue: Quick-witted and nimble, the cunning rogue moves through the shadows like a whisper. They are experts at lockpicking and sleight of hand, and always have a trick up their sleeve. \nAre you certain") 
  elif choice == "D" or choice == "d":
    print ("D - The Wise Elder: With a long white beard and piercing eyes, the wise elder is a font of knowledge and guidance. They have seen much in their long life and have many stories to tell. Though frail in body, their mind is sharp and their spirit unbroken. \nAre you certain?")
  elif choice == "E" or choice == "e":
    print ("E - Dylan the obnoxious bard: A wiley and charasmatic character that has been baned from more establishments than he patroned. His prowess with alcohol is matched only by his skill with maracas. He has no concept of personal space, boundries or, taste. \nAre you certain?")  
  else: anger()
  
  
  yn = input()
  if yn=='y' or yn=="Y":
    print ("Very well. Then procede")
  else: anger()
while yn == "n" or yn == "N":
  print ("well then be more certain than that.")



#this should not work with a sure regardless need a method to recurve to the top and restart the questions


print("\n\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n\n")


# Nev 

# Add selection text in here for the four choices

print("a - I wouldn't do that or would I?")
print("b - Hmmm? I don't know?")
print("c - Ok, not a bad option.")
print("d - Take my advice, turn back.")

Path2Takeoutput()

  
# Ty

print("You have four ways to pay the (ransom) tuition")
Payment()


#Placement
print("Welcome to the next task, which is placement:")
placement = int(input("If you are coming out of highschool, please enter a 1,\nIf you have been to college before and want to place out of classes and into more advanced ones, type a 2,\nIf you are unsure of what you are doing, but you think you are smart, type 3,\nIf you have no idea what you are doing here and need further help, type a 4\n"))
#asks the user to pick one of the four options

if placement == 1 or 2:
  print("Great, right this way, the process is very simple. You will come to campus tomorrow and take a few tests in the core subjects")
  #if the user is coming out of HS or has been to college, they are in the same placement process, they can test out of certain classes
elif placement == 3:
  print("Hello traveler, it seems that you have some wisdom, or so they say. You will be prompted to answer a math question, if you get it right, you may proceed to placement.")
  question = int(input("What is 9 + 10?")) #this is a funny way to mess with someone
  if question != 21:
    print("Try again")
    #make a loop here
else:
  print("If you do not know what is going on here, please visit the EVCC Placement website.")
  #link to evcc website


#advising

Print("The next step is advising, you are almost there Mr or Misses Traveler. Fortunately you get an advisor to help you with the rest of your journey.")
advisor = int(input("pick a number between 1 & 4 please:"))
#the user picks a random number and that reflects their advisor
#we said dog, donkey, fish bowl


