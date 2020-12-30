# Import art and game_data and random
import random
from art import logo, vs
from game_data import data

# Make a list for A and B
fighters = []

# set A and B
fighters = random.sample(data, 2)

# Print logo
print(logo)

# set user score
score = 0

# Print A
print(f"Compare A: {fighters[0]['name']}, a  {fighters[0]['description']}, from  {fighters[0]['country']}.")

# Print VS and B
print(vs)
print(f"Against B: {fighters[1]['name']}, a  {fighters[1]['description']}, from  {fighters[1]['country']}.")

# Make function to compare A and B
# and return which won.
def compare(a, b):
  if a > b:
    return 'A'
  else:
    return 'B'


# set if user continue
is_gameover = False

while not is_gameover:
  # Ask user which choose A or B, and store choose data
  choose = input("Who has more followers? Type 'A' or 'B': ")

  answer = compare(fighters[0]['follower_count'], fighters[1]['follower_count'], )

  if choose == answer:
    print('You win')
  else:
    print(f"Sorry, that's wrong. Final score: {fighters[0]['follower_count']}")
    is_gameover = True
      


  # If user won, update list 
  # else print Sorry, that's wrong. Final score:
