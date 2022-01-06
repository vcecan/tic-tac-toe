###################           ###################                    ####################
        ##   ##     #####             ##     ###### ##     #####              ##     #######       ######
        ##         ##    ##           ##    ##    ## #    ##    ##            ##    ##     ##    ##     ##
        ##   ##   ##                  ##   ##      ###   ##                   ##   ##       ##   ##     ##
        ##   ##   ##        #######   ##   ##      ###   ##         #######   ##   ##       ##   ########
        ##   ##   ##                  ##   ##      ###   ##                   ##   ##       ##   ##
        ##   ##    ##    ##           ##    ##    ## #    ##    ##            ##    ##     ##    ##     #
        ##   ##     ######            ##     ###### ##     ######             ##     #######      ######

####################################################################################################################
from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
import os
import sys


sys.setrecursionlimit(9000)
infinity = 1000
opponent = 'O'
player = 'X'





level_count=0

root = Tk()
root.configure(bg='#030f18')
# text = [[None]*3 for _ in range(3)]
b = [[""] * 3 for _ in range(3)]
clicked = True



def table_grid():
    global board, poz_list
    for i in range(3):
        for j in range(3):
            b[i][j].grid(row=i, column=j)
    restart.grid(row=3,column=0)
    board = [[None] * 3 for _ in range(3)]
    poz_list = []
    for i in range(9):
        poz_list.append(i)
        



def player_vs_cpu():

    label.grid(row=0, column=0,columnspan=3)
    e4.grid(row=1, column=1)
    e5.grid(row=2, column=1,pady=10)
    e6.grid(row=3, column=1,pady=(0,40))


def easy_level():
    e4.after(4, e4.destroy)
    e5.after(5, e5.destroy)
    e6.after(6, e6.destroy)
    label.after(7, label.destroy())
    table_grid()


def medium_level():
    e4.after(4, e4.destroy)
    e5.after(5, e5.destroy)
    e6.after(6, e6.destroy)
    label.after(7, label.destroy())
    table_grid()


def hard_level():
    e4.after(4, e4.destroy)
    e5.after(5, e5.destroy)
    e6.after(6, e6.destroy)
    label.after(7, label.destroy())
    table_grid()

def restart_click(restart):
    if clicked == True:
        python = sys.executable
        os.execl(python, python, *sys.argv)




def e_click(e):
    global level_count
    if e["text"] == "Easy" and clicked == True:
        easy_level()
        level_count = 4
    if e["text"] == "Medium" and clicked == True:
        medium_level()
        level_count = 5
    if e["text"] == "Hard" and clicked == True:
        hard_level()
        level_count = 6


########## game mode

letters = ['X', 'O']

def equals3(a, b, c):
    return a == b and b == c and a != ''


def checkWinner():
    global winner
    winner = False

    # horizontal
    for j in letters:
        for i in range(3):
            if (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == j):
                b[i][0].config(bg='#145a92')
                b[i][1].config(bg='#145a92')
                b[i][2].config(bg='#145a92')
                messagebox.showinfo("Congrats!!", "'" + j + "' has won")
                winner = True
                reset()
            if ( b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] == j):
                b[0][i].config(bg='#145a92')
                b[1][i].config(bg='#145a92')
                b[2][i].config(bg='#145a92')
                messagebox.showinfo("Congrats!!", "'" + j + "' has won")
                winner = True
                reset()
        if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == j):
            b[0][0].config(bg='#145a92')
            b[1][1].config(bg='#145a92')
            b[2][2].config(bg='#145a92')
            messagebox.showinfo("Congrats!!", "'" + j + "' has won")
            winner = True
            reset()
        if (b[0][2]["text"] == b[1][1]["text"] == b[2][0][
            "text"] == j):
            b[0][2].config(bg='#145a92')
            b[1][1].config(bg='#145a92')
            b[2][0].config(bg='#145a92')
            messagebox.showinfo("Congrats!!", "'" + j + "' has won")
            winner = True
            reset()

    if (count == 9 and winner == False):
        messagebox.showinfo("Tie!!", 'DRAW!')
        reset()
        winner= False



def move_true():
    global board
    for i in range(3):
        for j in range(3):
            if (board[i][j] ==None):
                return True
    return False



def evaluate():
    # Checking for Rows for X or O victory.
    global board
    for row in range(0, 3):

        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:

            if board[row][0] == 'X':
                return -10
            elif board[row][0] == 'O':
                return 10

    # Checking for Columns for X or O victory.
    for col in range(0, 3):

        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:

            if board[0][col] == 'X':
                return -10
            elif board[0][col] == 'O':
                return 10

    # Checking for Diagonals for X or O victory.
    if board[0][0] == board[1][1] and board[1][1] == b[2][2]:

        if board[0][0] == 'X':
            return -10
        elif board[0][0] == 'O':
            return 10

    if board[0][2] == board[1][1] and board[1][1] == b[2][0]:

        if board[0][2] == 'X':
            return -12
        elif board[0][2] == 'O':
            return 12

    # Else if none of them have won then return 0
    return 0


def reset():
    global count, board
    count = 0
    for i in range(9):
        poz_list.append(i)
    for i in range(3):
        for j in range(3):
            b[i][j].config(text=' ',bg='#030f18')
            board[i][j] = None


def comprandom():
    global avaible, board, count
    avaible = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                avaible.append((i, j))
    print(avaible)
    random_move = random.choice(avaible)
    b[random_move[0]][random_move[1]].config(text='O',fg='#F2003C')
    board[random_move[0]][random_move[1]] = "O"
    print(board)
    count = count + 1
    bestMove = findBestMove(board)
    print("The Optimal Move is :")
    print("ROW:", bestMove[0], " COL:", bestMove[1])


def ai_move():
    global board,count,bestMove
    if count==1:
        if board[1][1]==None:
            board[1][1]=opponent
            b[1][1].config(text='O',fg='#F2003C')
            count+=1
        elif count==1 and board[1][1]!=None:
            bestMove = findBestMove(board)
            b[bestMove[0]][bestMove[1]].config(text="O",fg='#F2003C')
            board[bestMove[0]][bestMove[1]] = opponent
            count = count + 1
    elif count >2:
        if count==3 and board[1][1]=='X' and board[2][2]=='X':
            b[0][2].config(text="O", fg='#F2003C')
            board[0][2] = opponent
            count=count + 1
        elif count==3 and board[0][2]=='X' and board [2][0]=='X':
            if board[2][1]==None:
                b[2][1].config(text="O", fg='#F2003C')
                board[2][1] = opponent
                count=count + 1
        elif count==3 and board[1][2]=='X' and board [2][1]=='X':
            if board[2][2]==None:
                b[2][2].config(text="O", fg='#F2003C')
                board[2][2] = opponent
                count=count + 1
        elif count==3 and board[0][1]=='X' and board [1][2]=='X':
            if board[0][2]==None:
                b[0][2].config(text="O", fg='#F2003C')
                board[0][2] = opponent
                count=count + 1
        elif count==3 and board[0][1]=='X' and board [1][2]=='X':
            if board[0][2]==None:
                b[0][2].config(text="O", fg='#F2003C')
                board[0][2] = opponent
                count=count + 1
        elif count==3 and board[1][0]=='X' and board [2][1]=='X':
            if board[2][0]==None:
                b[2][0].config(text="O", fg='#F2003C')
                board[2][0] = opponent
                count=count + 1
        elif count==3 and board[0][1]=='X' and board [1][0]=='X':
            if board[0][0]==None:
                b[0][0].config(text="O", fg='#F2003C')
                board[0][0] = opponent
                count=count + 1
        elif count==5 and board[1][1]== board[0][2] and board [0][2]=='X' and board[2][0]==None:
            b[2][0].config(text="O", fg='#F2003C')
            board[2][0] = opponent
            count=count + 1
        elif count==5 and board[1][1]== board[2][0] and board [2][0]=='X' and board[0][2]==None:
            b[0][2].config(text="O", fg='#F2003C')
            board[0][2] = opponent
            count=count + 1
        elif count == 5 and board[1][2] == board[2][1] and board[1][2] == 'X' and board[2][2] == 'X':
            b[0][2].config(text="O", fg='#F2003C')
            board[0][2] = opponent
            count = count + 1
        else:
            bestMove = findBestMove(board)
            if board[bestMove[0]][bestMove[1]]==None:
                b[bestMove[0]][bestMove[1]].config(text="O",fg='#F2003C')
                board[bestMove[0]][bestMove[1]] = opponent
                count = count + 1
                print("The Optimal Move is :")
                print("ROW:", bestMove[0], " COL:", bestMove[1])



def minimax(board, depth, isMax):
    score = evaluate()

    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 10):
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -10):
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (move_true() == False):
        return 0

    # If this maximizer's move
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == None):
                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board,depth + 1,isMax))

                    # Undo the move
                    board[i][j] = None
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == None):
                    # Make the move
                    board[i][j] = player

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1,not isMax))

                    # Undo the move
                    board[i][j] = None
        return best


# This will return the best possible move for the player
def findBestMove(board):
    bestVal = -1000
    bestMove = (1, 1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] == None):

                # Make the move
                board[i][j] = opponent

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = None

                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    return bestMove

count = 0


def b_click(i, j):
    global pozits, poz_list, avaible, level_count
    global count, clicked, currentplayer
    if board[i][j] == None:
        b[i][j].config(text='X',fg='#4B92DB')
        board[i][j] = player
        count = count + 1
        print(level_count)
        if count == 9:
            checkWinner()
        if count < 9:
            if level_count == 4:
                comprandom()
                checkWinner()
            if level_count == 5:
                if ((count+3)/2)%2==0:
                    comprandom()
                    checkWinner()
                elif ((count+3)/2)%2==1:
                    ai_move()
                    checkWinner()
            elif level_count==6:
                ai_move()
                checkWinner()
            print(board)

for i in range(3):
    for j in range(3):
        b[i][j] = Button(root, text=' ',fg=None,image=None, font=("Berlin Sans FB Demi",48 ), height=2, width=6, bg='#030f18',relief=GROOVE,highlightcolor= "white", activebackground='#145a92',bd=8,command=lambda i=i, j=j: b_click(i, j))


#Resize the Image using resize method

label=Label(text="TIC-TAC-TOE",font=('Cooper Black',20),fg='#1e87db',height=9,width=32,bg='#030f18')

e4 = Button(root, text="Easy", font=("Berlin Sans FB Demi", 26),fg='white', height=2, width=12, bg="#145a92",
            command=lambda: e_click(e4))
e5 = Button(root, text="Medium", font=("Berlin Sans FB Demi", 26),fg='white', height=2, width=12, bg="#145a92",
            command=lambda: e_click(e5))
e6 = Button(root, text="Hard", font=("Berlin Sans FB Demi", 26),fg='white', height=2, width=12, bg="#145a92",
           command=lambda: e_click(e6))
restart= Button(root, text='Reset',font=("Berlin Sans FB Demi", 10),fg='white', height=1, width=4, bg="#145a92",command=lambda: restart_click(restart))

player_vs_cpu()

root.mainloop()