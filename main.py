# Import art and game_data and random
import random
from art import logo, vs
from game_data import data
from replit import clear

# Make a list for A and B
fighters = []

# set A and B
fighters = random.sample(data, 2)

# set user score
score = 0

# Make function to compare A and B and return which won.
def compare(a, b):
  if a > b:
    fighters.pop(1)
    return 'A'
  else:
    fighters.pop(0)
    return 'B'


# Update Function
def update():
  fighters.append(random.choice(data))

# Print logo
print(logo)

# set if user continue
is_gameover = False

while not is_gameover:

  # Print A
  print(f"Compare A: {fighters[0]['name']}, a  {fighters[0]['description']}, from  {fighters[0]['country']}.")

  # Print VS and B
  print(vs)
  print(f"Against B: {fighters[1]['name']}, a  {fighters[1]['description']}, from  {fighters[1]['country']}.")

  # Ask user which choose A or B, and store chosen data
  choose = input("Who has more followers? Type 'A' or 'B': ")

  answer = compare(fighters[0]['follower_count'], fighters[1]['follower_count'], )

  print(fighters)

  if choose == answer:
    score += 1
    update()
      
    clear()
    print(logo)
    print(f"You are right! Current score: {score}")
    
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    is_gameover = True



