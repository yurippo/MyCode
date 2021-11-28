rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock Paper Scissor Game!\n")

choice = input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.")

if choice == "0":
  print(rock)

if choice == "1":
  print(paper)

if choice == "2":
  print(scissors) 

print("Computer choose") 

randomChoice = random.randint(0,2)

if randomChoice == 0:
  print(rock)

if randomChoice == 1:
  print(paper)

if randomChoice == 2:
  print(scissors) 

