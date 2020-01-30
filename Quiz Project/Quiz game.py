import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("What is (void*)0?", "Representation of NULL pointer", ["Representation of void pointer", "Error"]),
QA("In which header file is the NULL macro defined?", "stdio.h and stddef.h", ["stdio.h", "stddef.h", "math.h"]),
QA("A pointer is?", "A variable that stores address of other variable", ["A keyword used to create variables", "A variable that stores address of an instruction", "All of the above"]),
QA("The operator used to get value at address stored in a pointer variable is?", "*", ["&", "&&"]),
QA("The keyword used to transfer control from a function back to the calling function is?", "return", ["goto", "switch", "getch"])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("---------------------------")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("---------------------------")
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That is not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while  (userAnsw >= int(len(possible))):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = int(input())
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer is wrong.")
    print("Correct answer : " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")