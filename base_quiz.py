#base quiz learning code, this is the template i based mycode from

#importing the random libary 
import random

#globals and questions lists
score = 0
english = ["computer", "lake", "food"]
print(english[1])
right_answer = ["rorohiko", "roto", "kai"]
option_1 = ["wrong answer", "wrong answer", "wrong answer"]
option_2 = ["wrong answer", "wrong answer", "wrong answer"]

#define a function to generate a question
def generate_question(english,right_answer, option_1,option_2):
  global score
  print("what is the correct word for ", english, "in maori")
  #generate a random number to determine the  sequence of questions
  random_sequence = random.randint(0,2)
#seperate print statments for readability
  if (random_sequence == 0):
    print("A", option_1)
    print("b", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
  elif (random_sequence == 1):
    print("A", option_1 )
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
  elif (random_sequence == 2):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
  else:
    print ("incorrect")

for i in range (0,3):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
#pritns score
print ("ur score is",score)


print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
