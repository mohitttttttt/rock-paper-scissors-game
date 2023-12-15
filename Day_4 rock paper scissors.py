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

images= [rock, paper, scissors]

player_input = int(input("What do you choose? Type 0 for rocks, 1 for paper, 2 for scissors.\n"))

if player_input >=3 or player_input<0:
  print ("Invalid choice")

else:
  print ("You chose:" , images[player_input])
  
  comp_input = random.randint(0,2)
  print ("computer choose", images[comp_input])
  
  if player_input == comp_input:
    print ("It is a draw")
  
  elif player_input == 2 and comp_input == 0:
    print ("You lose")
  
  elif player_input > comp_input:
    print ("You win")
  
  elif player_input == 0 and comp_input == 2:
    print ("You win")
  
  elif player_input < comp_input:
    print ("You lose")
  