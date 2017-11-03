
import random
import time


   

def magic8():

  print("Thanks for wasting 10 seconds of my time in bed...")
  time.sleep(3)

  print("Right,wudda you want?")
  time.sleep(3)

  print("We don't need these answers,just keeping you entertained")
  time.sleep(3)

  age = input("How old are you?")

  food = input("What is your favourite food?")

  input("Ask the mighty 8 ball a question...")
  a = "Without a doubt"
  b = "Definetely"
  c = "No chance"
  d = "Good luck with that ambition (sarcasm)"
  e = "Get an actual Genie, not one inside a hard drive"
  f = "'m meeting the demands of many now.Call later"
  g = "Maybe"
  h = "Definetely not"

  choice = (random.randint(1, 8))

  
  if choice == 1:
    answer = a
  elif choice == 2:
    answer = b
  elif choice == 3:
      answer = c 
  elif choice == 4:
        answer = d
  elif choice == 5:
          answer = e 
  elif choice == 6:
            answer = f 
  elif choice == 7:
              answer = g
  else:
                  answer = h

  print("\nRacking my CPU..."*3)

  time.sleep(3)

  print("Here comes the long awaited answer...")
  time.sleep(5)

  print(answer)

  
  

def guessgame():

  attempts = 1

  secret_number = random.randint(1,100)
  isCorrect = False

  guess = int(input("Take a guess: "))


  while secret_number != guess and attempts < 6:


    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    guess = int(input("Take a guess: "))
    attempts += 1

  if attempts == 6:
    print("\nSorry you reached the maximum number of tries")
    print("The secret number was ",secret_number) 

  else:
    print("\nYou guessed it! The number was " ,secret_number)
    print("You guessed it in ", attempts,"attempts")
  input("\n\n Press the enter key to exit")   


def dice():

  min = 1
  max = 6

  roll_again = "yes"
  while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dices again?")

    
    
    
def sentencegen():
  def actualgen():
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "gently", "loyally", "primarily", "roughly", "significantly")
    adj = ("Adorable", "Clueless", "Dirty", "Odd", "Stupid", "Huge", "Cuddly", "Sudden", "Chivalrous", "Slimy", "Perfect", "Normal", "Smart")
    num = random.randrange(0, 5)
    print(nouns[num] + ' ' + verbs[num] + ' ' + adj[num] + ' ' + adv[num])
  for _ in range(1000000):
    actualgen()

def counting():

  print("Right, this next part of code was gonna count up to x number, but I'm gonna save you Windows XP, thank me later :)BTW, I Have the mock counting thing below, turn the 100000000000000000000000 into a more fathimable number to see it in action")
  a = 0
  while a <10000000000:
    a = a + 1

  print(a)
  a = 0
  while a < 100000: 
        a = a + 1
        print(a)


def menu():
  print("This magic 8 Ball can tell you the time (to the minute),\n it can answer questions,\n you can play games with it,\n itroll a dice \n and also count up to a number bigger than the time in lightyears the universe has been around for!\nType help into the program to get to grips on how to start the program...\n\n")
 
  print("\nFor the time, type 1.\n For the actual 8 ball, type 2().\n For the guessing game, type 3.\n For the dice type 4\n To count type 5 \n To generate a random sentence, type 6 \n To exit, type 7\nTo encode text using the caesar cipher type 8\n")


  selection =int(input("Please make your selection"))
  if selection == 1:
    timenow()
  elif selection == 2:
      magic8()
  elif selection == 3:
        guessgame()
  elif selection == 4:
          dice()
  elif selection == 5:
            counting()
  elif selection == 6:
              sentencegen()
  elif selection == 7:
                leave()
  elif selection == 8:
                  definition()
                  
                
kazooh = input("If you want to start, type start, if you want to leave, type leave")
if kazooh == ("start"):
  menu()
if kazooh == ("leave"):
  exit()
  
  
  
    
