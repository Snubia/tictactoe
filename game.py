#first we need a list comprehansion with 9 space. because we are lazy we won't make 9 spaces but just run a for loop

board = ["  " for i in range(9)]

#we will define a function to print the rows

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# We will make a fuction to define players moves and avoid repeating codes

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("your turn player {}".format(number))
    
    choice =int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == "  ":
        board[choice -1] = icon
    else:
        print()
        print("Sorry that space is taken!")

#now we will write a function to define the victory (winner)
        


def is_victory(icon):
    #we will check if they won per board rows then columns
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
          return True
    else:
        return False

def is_draw():
    #Let's include a draw feature for when nobody wins and all the boards are full

    if "  " not in board:
        return True
    else:
        return False

#we will now also use a while loop also called game loop. it runs for ever

    #condition to print the winner and that it going to end the game and break the while loop

while True:
    print_board()
    player_move("X")
    print_board()
    
    if is_victory("X"):
        print("Woohoo X wins! congratulations player!")
        break
    elif is_draw():
        print("Oh nooo it is a draw!")
        break
    
    player_move("O")
    
    if is_victory("O"):
        print_board()
        print("Woohoo O wins! congratulations player!")
        break
    elif is_draw():
        print("Oh nooo it is a draw!")
        break
   
    
