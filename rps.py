# rock, paper scissors Basic Version
# needs and else is for  r vs s, r vs p, s vs r, s vs p, p vs r, p vs s
# a bunch of lines that hide player 1 choice 'no cheating!'
# each player needs a prompt to choose between rps

# introduction
print("...rock...\n...paper...\n...scissors...!")

# get input from users
player1 = input("Player 1 choice: ")
print("\n NO CHEATING! \n" * 20) # just for fun
player2 = input("Player 2 choice: ")

# conditional
if (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Player 2 wins!")

# if player1 is "paper"
#     if player2 is "rock"
#         answer = "player 2 wins"
#     if player2 is "scissors"
#         answer = "player 1 wins"