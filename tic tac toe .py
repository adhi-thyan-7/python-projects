#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
bot = 'X'


# In[2]:


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('_____')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('_____')
    print(board[7] + '|' + board[8] + '|' + board[9])


# In[3]:


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


# In[4]:


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("oops space is occupied")
        position = int(input("enter new position:  "))
        insertLetter(letter, position)
        return


# In[ ]:


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


# # def checkDraw():
#     for key in board.keys():
#         if (board[key] == ' '):
#             return False
#     return True
# 
# def playerMove():
#     position = int(input("Enter the position for 'O':  "))
#     insertLetter(player, position)
#     return
# 
# def compMove():
#     position = int(input("Enter the position for 'X':  "))
#     insertLetter(bot, position)
#     return
# 
# printBoard(board)
# 
# 

# In[ ]:


while not checkForWin():
    compMove()
    playerMove()
    

