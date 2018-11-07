player1 = input('Player 1, make your choice: ')
player2 = input('Player 2, make your choice: ')


print('...rock...')
print('...paper...')
print('...scissors..')
print('...SHOOT!...')


if player1 == 'rock' and player2 == 'scissors':
    print('rock crushes scissors! player 1 wins!')
elif player1 == 'rock' and player2 == 'paper':
    print('paper covers rock! player 2 wins!')
elif player1 == 'paper' and player2 == 'scissors':
    print('scissors cut paper! player 2 wins!'))
elif player1 == 'paper' and player2 == 'rock':
    print('paper covers rock! player 1 wins!')
elif player1 == 'scissors' and player2 == 'rock':
    print('rock crushes scissors! player 2 wins!')
elif player1 == 'scissors' and player2 == 'paper':
    print('scissors cut paper! player 1 wins!')
elif player1 == player2:
    print('both players chose the same! its a tie!')
else:
    print('something went wrong')
