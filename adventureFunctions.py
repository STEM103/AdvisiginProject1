import random
def Payment():   
  Payment = int(input("pick a number between 1 & 4, if you pick 4 you will get a random path:"))

  if Payment == 4:
  # 6 paragraphs of info on finances that super complex (make it fantasy themed)
    Payment = random.randint(1,3)
  if Payment == 1:  
    print("You are on your own!")
  elif Payment == 2:
  # 3 paragraphs a bit a technical but reasonably 
    print("You get some resources to help pay the tuition")
  elif Payment == 3:
  # explain that they get free because [insert reason]
   print("You get free college")
  else:
    print("error Oxb8853934893")

#Neville
def Path2Takeoutput():
    print("a", "b", "c", "d")
    path = input("select your path")
    if path == "a":
     print("Welcome traveler! Here are some resources to help you on your journey.")
    if path == "b":
     print("Why are you here? Just wandering around?")
    if path == "c":
     print("This is the way.")
    if path == "d":
     print("Take the yellow brick road. You have nothing to worry about.")
    else: anger()



def anger():
  print("what have you done? How did you even get here? No seriously how did you find this. You should not be here what did you do. Go get one of the admins. No i don't care that I'm breaking character, you broke the code. go get an admin now.")
