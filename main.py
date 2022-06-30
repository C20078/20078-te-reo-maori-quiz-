#base quiz learning code

#importing the time libary 
import time
#importing the random libary 
import random


#globals and questions lists
score = 0
question = ["Red", "tribe", "greenstone","family","Childern","river","yellow","morepork","water","ocean","cold"]
translation = ["Whero", "iwi", "pounamu","whānau","Tamariki","awa","Kōwhai","Ruru","wai","moana", "kuiki "]
option_1 = ["Pākehā", "hongi ", "kakahu ","kokako ","pōkokohua","Rangatira","manuka", "pakipaki","rangi","tahi","poi"]
option_2 = ["taniwha", "tuatara", "tawa ","aroha","whetu","poi","korowai","harakeke","moa","kauri","maa"]

#this will cause code to print in green and bold font
print("\033[1;32m ")
#this is the introduction, it asks for your name and welcomes you to the quiz, it also includes instuctions and the option to not do the quiz. if you choose not to do the quiz the code with then end.
print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
time.sleep(1)
user = input ("Hello, What is your name? ") 
time.sleep(1)
print ("Kia ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge.")
time.sleep(1)
answer = input ("Do you want to take this quiz? yes/no [enter] \n").lower()

if answer == "yes":
  time.sleep(1)

else:
  print ("Okay, maybe next time")
  quit()
print ("To answer questions please type either A,B or C for the option you would like to choose then press [enter]")
time.sleep(2)
print()
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
time.sleep(2)
#define a function to generate a question
def generate_question(english,right_answer, option_1,option_2):
  global score
  #this will cause code to print in blue and bold font
  print("\033[1;34m ")
  #asks the question and genreates options for the question
  print("What is the correct word for", english, "in maori")
  #generate a random number to determine the  sequence of questions
  random_sequence = random.randint(0,2)
#seperate print statments for readability

  if (random_sequence == 0):
    print("A.", option_1)
    print("B.", option_2)
    print("C.", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct! your score =", score)
    else:
      print ("Incorrect, your score =", score)
  elif (random_sequence == 1):
    print("A.", option_1 )
    print("B.", right_answer)
    print("C.", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
      print("Correct! your score =", score)
    else:
      print ("Incorrect, your score =", score)
  elif (random_sequence == 2):
    print("A.", right_answer)
    print("B.", option_2)
    print("C.", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("Correct! your score =", score)
    else:
      print ("Incorrect, your score =", score)

for i in range (0,10):
  generate_question(question[i],translation[i],option_1[i],option_2[i])
#when all questions have been answered,thanks them for doinng the quiz aswell as saying they did well and showing them their overall score

print ("Your overall score is",score)
if score > 9:
  print ("You did well " + user + "\n"
      "(っ◔◡◔)っ ♥ You are amazing ♥")
else:
  print("Good Try")
time.sleep(1)
