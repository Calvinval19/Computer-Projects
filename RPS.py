#Description: This program simulates the game of Rock-Paper-Scissors against a computer. The user enters their choice of either "rock", "paper", or "scissors". The computer will generate a random number between 1 and 3. 1 equals to paper. 2 equals to rock. 3 equals to scissors. If the user wins against the computer, a message will appear saying the user has won. If the user loses against the comptuer, a message will appear stating the computer has won. IF the user does not put an option, a message will appear stating "Invalid Move!!".

import random


def main():
  choice = input("Please enter your move: paper, rock, scissors: ")
  computer = random.randint(1,3)
  
  if computer == 1:
    print("Computer's move is Paper")
  elif computer == 2:
    print("Computer's move is Rock")
  elif computer == 3:
    print("Computer's move is Scissors")
  
  if choice != 'rock' and choice != 'paper' and choice != 'scissor' and choice != 'scissors':
    print("Invalid Move!!")
  
  if computer == 1 and choice == "paper":
    print("Tie with Paper!")
  elif computer == 1 and choice == "rock":
    print("You lose! Paper beats Rock!")
  elif computer == 1 and choice == "scissors":
    print("You win! Scissors Cuts Paper")
  elif computer == 1 and choice == "scissor":
    print("You win! Scissors Cuts Paper")
  
  
  if computer == 2 and choice == "paper":
    print("You win! Paper beats Rock!")
  elif computer == 2 and choice == "rock":
    print("Tie with Rock!")
  elif computer == 2 and choice == "scissors":
    print("You lose! Rock Breaks Scissors!")
  elif computer == 2 and choice == "scissor":
    print("You lose! Rock Breaks Scissors!")
  
  if computer == 3 and choice == "paper":
    print("You lose! Scissors Cuts Paper!")
  elif computer == 3 and choice == "rock":
    print("You win! Rock Breaks Scissors!")
  elif computer == 3 and choice == "scissors":
    print("Tie with Scissors!")
  elif computer == 3 and choice == "scissor":
    print("Tie with Scissors!")

main()


'''Sample Output #1
Please enter your move: paper, rock, scissors: rock 
Computer's move is Scissors
You win! Rock Breaks Scissors!'''

'''Sample Output #2
Please enter your move: paper, rock, scissors: scissor
Computer's move is Rock
You lose! Rock Breaks Scissors!'''

'''Sample Output #3
Please enter your move: paper, rock, scissors: rubber band
Computer's move is Paper
Invalid Move!!'''