#MILESTONE PROJECT

#Função do tabuleiro

def display_board(board):
    
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])

 

        #display_board(game_board)

#Escolha do Player e armazenamento da escolha como váriavel

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Jogador 1, você deseja ser X ou O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

        #player_input()
     


#Substituição das strings do tabuleiro pela escolha dos players

def place_marker(board, marker, position):
    board[position] = marker

        #place_marker(test_board,'$',8)
        #display_board(test_board)

#Checar condição de vitória

def win_check(board, mark):
    
    return ((board[1] == mark and board[2]== mark and board[3]== mark) or   #LINHAS HORIZONTAIS
            (board[4] == mark and board[5]== mark and board[6]== mark) or   #LINHAS HORIZONTAIS
            (board[7] == mark and board[8]== mark and board[9]== mark) or   #LINHAS HORIZONTAIS
            (board[7] == mark and board[4]== mark and board[1]== mark) or   #LINHAS VERTICAIS
            (board[8] == mark and board[5]== mark and board[2]== mark) or   #LINHAS VERTICAIS
            (board[9] == mark and board[6]== mark and board[3]== mark) or   #LINHAS VERTICAIS
            (board[7] == mark and board[5]== mark and board[3]== mark) or   #DIAGONAIS
            (board[1] == mark and board[5]== mark and board[9]== mark))     #DIAGONAIS
            
        #print(win_check(test_board,'X'))

#Randomixador para decidir quem começa
import random

def randomizer():
    
    num = (random.randint(0, 1))

    if num ==0:
        return ('Jogador 1')
    else:
        return ('Jogador 2')
    
#Indicar se o espaço selecionado está vazio com um resultado booleano
def space_check(board, position):
    
    return board[position] == ' '

#Indicar se o tabuleiro ainda tem espaços

def board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    
       #print(board_check(test_board))

#Pede que o jogador escolha a próxima posição e utiliza space_check para indicar se a casa escolhida está vazia
def player_choice(board):
    position = 'wrong'      
    
    while position not in range(1,10):
        position = int(input('Escolha a próxima posição(1-9): '))
    
    while space_check(board, position) == False:
        position = int(input('Essa casa já foi utilizada, escolha outra posição!(1-9): '))
        
    return position

# Função de replay
def replay():
    
    return input('Deseja jogar novamente?: ').lower().startswith('s')

#################################################
print ('Bem vindo ao Jogo da Velha!')



while True:
    #resetar o tabuleiro
    tabuleiro = [' ']*10
    player1_marker, player2_marker = player_input()
    turno = randomizer()
    print (turno + ' irá começar!')
    
    play_game = input('Você está pronto para jogar? Digite sim ou não: ')
    if play_game.lower()[0] == 's':
        game_on = True
    else:
        game_on = False
    
    
    while game_on:  
        #Turno do Jogador 1
        if turno == 'Jogador 1':
            display_board(tabuleiro)
            position = player_choice(tabuleiro)
            place_marker(tabuleiro, player1_marker, position)
            
            if win_check(tabuleiro, player1_marker) == True:
                display_board(tabuleiro)
                print ('Parabéns, o Jogador 1 venceu!')
                game_on =  False
            else:
                if board_check(tabuleiro):
                    display_board(tabuleiro)
                    print ('Deu velha!')
                    break
                else:
                    turno = 'Jogador 2'
                    print ('Agora é a vez do Jogador 2')
        #Turno do Jogador 2
        else:
                display_board(tabuleiro)
                position = player_choice(tabuleiro)
                place_marker(tabuleiro, player2_marker, position)
                
                if win_check(tabuleiro, player2_marker) == True:
                    display_board(tabuleiro)
                    print ('Parabéns, O jogador 2 venceu!')
                    game_on = False
                else:
                    if board_check(tabuleiro):
                        display_board(tabuleiro)
                        print ('Deu velha!')
                        break
                    else:
                        turno = 'Jogador 1'
                        print ('Agora é a vez do Jogador 1')    
                        
    if not replay():
            break
            

    
   
    
    
