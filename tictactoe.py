
board = ['_','_','_',
         '_','_','_',
         '_','_','_']

game_is_in_session = True 

winner = None

current_player = 'X'


def display_board():
   print(board[0] + '|' + board[1] + '|' + board[2] + '|')
   print(board[3] + '|' + board[4] + '|' + board[5] + '|')
   print(board[6] + '|' + board[7] + '|' +  board[8] + '|')

def play_game():

  display_board()
 
  while game_is_in_session:

    handle_turn(current_player)

    player()

    check_for_game_over()

    flip_player()

  if winner == 'X' or winner == 'O' :
    print(' Winner is ' +  winner + '!')

  elif  winner == None:
    print('Tie')
    

def handle_turn(player):
  print(player + "'s turn .")  
  position = input('choose a vacant position from 1-9:')
  position = int(position) - 1
  
  board[position] = player

  display_board()
   
def player():
  return   


def check_for_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
 
  global winner

  row_winner = check_rows() 

  column_winner = check_columns()

  diagonal_winner = check_diagonals()

  if row_winner:
     winner = row_winner
  elif column_winner:
     winner = column_winner
  elif diagonal_winner:
      winner = diagonal_winner
  else:
      winner = None
       
  return   

def check_rows():

    global game_is_in_session

    row_1 = board[0] == board[1] == board[2]  != '_'
    row_2 = board[3] == board[4] == board[5]  != '_'
    row_3 = board[6] == board[7] == board[8]  != '_'

    if  row_1 or row_2 or row_3:
     game_is_in_session = False

    if row_1 :
     return board[0] 
    elif row_2:
     return board[3] 
    elif row_3 :
     return board[6] 

    return

def check_columns():
    
    global game_is_in_session

    column_1 = board[0] == board[3] == board[6]  != '_'
    column_2 = board[1] == board[4] == board[7]  != '_'
    column_3 = board[2] == board[5] == board[8]  != '_'

    if  column_1 or column_2 or column_3:
     game_is_in_session = False

    if column_1 :
     return board[0] 
    elif column_2:
     return board[1] 
    elif column_3 :
     return board[2] 

    return

def check_diagonals():
    global game_is_in_session

    diagonal_1 = board[0] == board[4] == board[8]  != '_'
    diagonal_2 = board[2] == board[4] == board[6]  != '_'
    

    if  diagonal_1 or diagonal_2:
     game_is_in_session = False

    if diagonal_1 :
     return board[0] 
    elif diagonal_2:
     return board[2] 
    

    return          

def check_if_tie():
  global game_is_in_session
  if '_' not in board:
      game_is_in_session = False

  return

def flip_player():
  global current_player  
  if current_player == 'X':  
      current_player = 'O'

  elif current_player == 'O':
      current_player = 'X'    
  return 

play_game()