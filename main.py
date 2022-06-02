# import random module
import random


print("Winning rules of the Rock paper scissors game are as follows: \n"
+ "Rock vs paper -> Paper wins \n"
+ "Rock vs scissors ->Rock wins \n"
+ "paper vs scissors ->Scissors win \n")

moves = ['R', 'P', 'S']
randomNumber = random.randint(0, 2)
cpuMove = moves[randomNumber]

while True:
    player = input('Type R for Rock/ P for paper/ S for scissors or Q to quit: \n').upper()
    if player == 'Q':
        break
    elif player not in moves:
        print('Invalid option, try again\n')
        continue

    if player == cpuMove:
        if player == cpuMove == 'R':
            print('Player (Rock) : CPU (Rock)\n')
            print('Tie')

        elif player == cpuMove == 'P':
            print('Player (Paper) : CPU (Paper)\n')
            print('Tie')

        elif player == cpuMove == 'S':
            print('Player (Scissors) : CPU (Scissors)\n')
            print('Tie')
    
    elif player == 'R':
        if cpuMove =='P':
            print('Player (Rock) : CPU (Paper)\n')
            print('You lose')
        elif cpuMove == 'S':
            print('Player (Rock) : CPU (Scissors)\n')
            print('You win')

    elif player == 'P':
        if cpuMove == 'S':
            Print('Player (Paper) : CPU (Scissors)\n')
            print('You lose')
        elif cpuMove == 'R':
            print('Player (Paper) : CPU (Rock)\n')
            print('You win')

    elif player == 'S':
        if cpuMove == 'R':
            print('Player (Scissors) : CPU (Rock)\n')
            print('You lose')
        elif cpuMove == 'P':
            print('Player (Scissors) : CPU (Paper)\n')
            print('You win')

    

    