from tkinter import *
from tkinter import ttk 
import tkinter.messagebox

board={1:' ',2:' ',3:' ',
      4:' ',5:' ',6:' ',
      7:' ',8:' ',9:' ',}

level=1
def checkDraw():
    for key in board:
        if board[key]==' ':
            return False
    else:
        return True
def checkWhowon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] ==mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] ==mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] ==mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] ==mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] ==mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] ==mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1]==mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] ==mark):
        return True
    else:
        return False
    

def evaluate_board(board):
    if checkWhowon('O'):
        return 1
    elif checkWhowon('X'):
        return -1
    elif checkDraw():
        return 0
    else:
        return 0 #default value


# def value(board,depth,isMaximising,alpha,beta):
#     # if checkWhowon('O'):
#     #     return 1
#     # elif checkWhowon('X'):
#     #     return -1
#     # elif checkDraw():
#     #     return 0
#     evaluate_board(board)
#     if isMaximising:
#         return max_value(board,depth,alpha,beta)
#     else:
#         return min_value(board,depth,alpha,beta)

def value(board, depth, isMaximising, alpha, beta):
    if isMaximising:
        return max_value(board, depth, alpha, beta)
    else:
        return min_value(board, depth, alpha, beta)


def max_value(board, depth, alpha, beta):
    if depth == 0 or checkWhowon('O') or checkWhowon('X') or checkDraw():
        #heuristic value with evaluation function
        return evaluate_board(board)
    else:
        bestScore = -1000
        for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'O'
                    score = value(board, depth-1, False, alpha, beta)
                    board[key] = ' '
                    bestScore = max(bestScore, score)
                    alpha = max(alpha, bestScore)  
                    if bestScore >= beta:
                        break 
        return bestScore
    

def min_value(board,depth, alpha, beta):
    if depth == 0 or checkWhowon('O') or checkWhowon('X') or checkDraw():
        return evaluate_board(board)
    else:
        bestScore = 1000
        for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'X'
                    score = value(board, depth-1, True, alpha, beta)
                    board[key] = ' '
                    bestScore = min(bestScore, score)
                    beta = min(beta, bestScore)  
                    if bestScore <= alpha:
                        break  
        return bestScore
      
    
    
""" def minimax(board,depth,isMaximising,alpha,beta):
    if checkWhowon('O'):
        return 1
    elif checkWhowon('X'):
        return -1
    elif checkDraw():
        return 0
    if isMaximising:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, depth, False, alpha, beta)
                board[key] = ' '
                bestScore = max(bestScore, score)
                alpha = max(alpha, bestScore)  
                if bestScore >= beta:
                    break  
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, 0, True, alpha, beta)
                board[key] = ' '
                bestScore = min(bestScore, score)
                beta = min(beta, bestScore)  # Update beta
                if bestScore <= alpha:
                    break  # Pruning condition
        return bestScore
"""
# def both():
#     alpha=-1000
#     beta=1000
#     bestScore = -1000
#     bestMove =1
#     for key in board.keys():
#         if (board[key]==' '):
#             board[key]='O'
#             score=value(board,9,False,alpha,beta)
#             board[key]=' '
#             if score > bestScore:
#                 bestScore= score
#                 bestMove= key           
#     return bestMove


# def bote():
#      alpha=-1000
#      beta=1000
#      bestScore = -1000
#      bestMove =1
#      for key in board.keys():
#         if (board[key]==' '):
#             board[key]='O'
#             score=value(board,2,False,alpha,beta)
#             board[key]=' '
#             if score > bestScore:
#                 bestScore= score
#                 bestMove= key           
#      return bestMove

# def botm():
#             alpha=-1000
#             beta=1000
#             bestScore = -1000
#             bestMove =1
#             for key in board.keys():
#                 if (board[key]==' '):
#                     board[key]='O'
#                     score=value(board,4,False,alpha,beta)
#                     board[key]=' '
#                     if score > bestScore:
#                         bestScore= score
#                         bestMove= key           
#             return bestMove


def bot(depth):
    alpha = -1000
    beta = 1000
    bestScore = -1000
    bestMove = 1
    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'O'
            score = value(board, depth, False, alpha, beta)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    return bestMove


def cliquer(nb):
    global ecran 
    ecran=ecran +str(nb)
    Affichage.set(ecran)
def ouvrirxo():

    def ButtonClick(loc):
        global a,b,c,board,level
        print("level: ", level)
        print("ID:{}".format(loc))
        if loc==1  and boutton1['text']==' '  and a==1:
            boutton1['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==2 and boutton2['text']==' ' and a==1:
            boutton2['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==3 and boutton3['text']==' ' and a==1:
            boutton3['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==4 and boutton4['text']==' ' and a==1:
            boutton4['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==5 and boutton5['text']==' ' and a==1:
            boutton5['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==6 and boutton6['text']==' ' and a==1:
            boutton6['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==7 and boutton7['text']==' ' and a==1:
            boutton7['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==8 and boutton8['text']==' ' and a==1:
            boutton8['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1
        if loc==9 and boutton9['text']==' ' and a==1:
            boutton9['text']="X"
            board[loc]="X"
            a=0
            if level==0:
                loc=bot(9)
            elif level==1:
                loc=bot(5)
            elif level==2:
                loc=bot(2)
            b+=1

        if loc==1 and boutton1['text']==' ' and a==0:
            boutton1['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==2 and boutton2['text']==' ' and a==0:
            boutton2['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==3 and boutton3['text']==' ' and a==0:
            boutton3['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==4 and boutton4['text']==' ' and a==0:
            boutton4['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==5 and boutton5['text']==' ' and a==0:
            boutton5['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==6 and boutton6['text']==' ' and a==0:
            boutton6['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==7 and boutton7['text']==' ' and a==0:
            boutton7['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==8 and boutton8['text']==' ' and a==0:
            boutton8['text']="O"
            board[loc]="O"
            a=1
            b+=1
        if loc==9 and boutton9['text']==' ' and a==0:
            boutton9['text']="O"
            board[loc]="O"
            a=1
            b+=1
            
           
        if( boutton1['text']=='X' and boutton2['text']=='X' and boutton3['text']=='X' or
            boutton4['text']=='X' and boutton5['text']=='X' and boutton6['text']=='X' or
            boutton7['text']=='X' and boutton8['text']=='X' and boutton9['text']=='X' or
            boutton1['text']=='X' and boutton4['text']=='X' and boutton7['text']=='X' or
            boutton2['text']=='X' and boutton5['text']=='X' and boutton8['text']=='X' or
            boutton3['text']=='X' and boutton6['text']=='X' and boutton9['text']=='X' or
            boutton1['text']=='X' and boutton5['text']=='X' and boutton9['text']=='X' or
            boutton3['text']=='X' and boutton5['text']=='X' and boutton7['text']=='X'):
                c=1
                tkinter.messagebox.showinfo("xo","Le gagnant est le joueur")
                restartbutton()
        elif( boutton1['text']=='O' and boutton2['text']=='O' and boutton3['text']=='O' or
            boutton4['text']=='O' and boutton5['text']=='O' and boutton6['text']=='O' or
            boutton7['text']=='O' and boutton8['text']=='O' and boutton9['text']=='O' or
            boutton1['text']=='O' and boutton4['text']=='O' and boutton7['text']=='O' or
            boutton2['text']=='O' and boutton5['text']=='O' and boutton8['text']=='O' or
            boutton3['text']=='O' and boutton6['text']=='O' and boutton9['text']=='O' or
            boutton1['text']=='O' and boutton5['text']=='O' and boutton9['text']=='O' or
            boutton3['text']=='O' and boutton5['text']=='O' and boutton7['text']=='O'):
                c=1
                tkinter.messagebox.showinfo("xo","Le gagnant est le BOT")
                restartbutton()
        elif b==9:
                c=1
                tkinter.messagebox.showinfo("xo","Egalite!")
                restartbutton()

        if a==1 and c==0:
            playerturn['text']="  Le tour du joueur  "
        elif a==0 and c==0:
            playerturn['text']=" Le tour de BOT "
    def restartbutton():
        global a,b,c,board
        a=1
        b=0
        c=0
        board={1:' ',2:' ',3:' ',
                4:' ',5:' ',6:' ',
                7:' ',8:' ',9:' ',}
        playerturn['text']="   Le tour du joueur  "
        boutton1['text']=' '
        boutton2['text']=' '
        boutton3['text']=' '
        boutton4['text']=' '
        boutton5['text']=' '
        boutton6['text']=' '
        boutton7['text']=' '
        boutton8['text']=' '
        boutton9['text']=' '



    xo=Toplevel(fenetre)
    xo.title("XO")
    boutton1=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
    boutton1.config(command=lambda: ButtonClick(1))
    boutton2=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
    boutton2.config(command=lambda: ButtonClick(2))
    boutton3=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
    boutton3.config(command=lambda: ButtonClick(3))
    boutton4=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
    boutton4.config(command=lambda: ButtonClick(4))
    boutton5=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
    boutton5.config(command=lambda: ButtonClick(5))
    boutton6=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
    boutton6.config(command=lambda: ButtonClick(6))
    boutton7=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
    boutton7.config(command=lambda: ButtonClick(7))
    boutton8=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
    boutton8.config(command=lambda: ButtonClick(8))
    boutton9=Button(xo,text=' ',bd=8, fg="black",font=('arial', 20,'bold'),bg="grey")
    boutton9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
    boutton9.config(command=lambda: ButtonClick(9))
    playerturn=Label(xo,text="   Le tour du joueur  ",bd=8, fg="black",font=('arial', 10,'bold'),bg="white")
    playerturn.grid(row=3,column=0,sticky='snew',ipadx=10,ipady=10)
    playerdetails=Label(xo,text="    Le joueur est X\n\n    Le BOT est O",bd=8, fg="black",font=('arial', 7,'bold'),bg="white")
    playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)
    res=Button(xo,text='Rejouer',bd=8, fg="black",font=('arial', 10,'bold'),bg="green")
    res.grid(row=3,column=1,sticky='snew',ipadx=50,ipady=50)
    res.config(command=lambda: restartbutton())



    xo.mainloop()


def hardbutton():
        global level
        level=0
        return ouvrirxo()
        
def mediumbutton():
        global level
        level=1
        return ouvrirxo()

def easybutton():
        global level
        level=2
        return ouvrirxo()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
fenetre=Tk()
fenetre.title('Platform Menu')
page_Bienvenue = ttk.Frame(fenetre,relief = SUNKEN) 
page_Bienvenue["padding"]=(20,20)

Acceuil_1=ttk.Label(page_Bienvenue,text='Bienvenue sur XO.',foreground='black',font=('Helvetica',16))
if Acceuil_1:
    # Use the grid geometry manager to center the label
    Acceuil_1.grid(row=0, column=1, padx=10, pady=10)
else:
    print("Error: Label not created successfully")
#Acceuil_1.pack(side="top", fill="both", expand=True)

# Center the window on the screen
#center_window(fenetre)
#XO_Button=Button(page_Bienvenue,bd=40, fg="black",font=('arial', 20,'bold'),text="Jeu XO",bg="White").grid(row=1,column=1)
XO_Label = ttk.Label(page_Bienvenue, text="Jeu XO", foreground='black', font=('arial', 20, 'bold'))
XO_Label.grid(row=1, column=1)
hard=Button(page_Bienvenue,text='Hard',bd=8, fg="black",font=('arial', 20,'bold'),bg="red")
hard.grid(row=2,column=0,sticky='snew',ipadx=60,ipady=60)
hard.config(command=lambda: hardbutton())
medium=Button(page_Bienvenue,text='Medium',bd=8, fg="black",font=('arial', 20,'bold'),bg="orange")
medium.grid(row=2,column=1,sticky='snew',ipadx=60,ipady=60)
medium.config(command=lambda: mediumbutton())
easy=Button(page_Bienvenue,text='Easy',bd=8, fg="black",font=('arial', 20,'bold'),bg="yellow")
easy.grid(row=2,column=2,sticky='snew',ipadx=60,ipady=60)
easy.config(command=lambda: easybutton())

ecran= ""
Affichage= StringVar()
a=1
b=0
c=0

page_Bienvenue.grid(row=0,column=0)
Acceuil_1.grid(row=0,column=0,padx=10,pady=10)
fenetre.mainloop()


"""    hard=Button(xo,text='Hard',bd=8, fg="black",font=('arial', 10,'bold'),bg="red")
    hard.grid(row=4,column=0,sticky='snew',ipadx=60,ipady=60)
    hard.config(command=lambda: hardbutton())
    medium=Button(xo,text='Medium',bd=8, fg="black",font=('arial', 10,'bold'),bg="orange")
    medium.grid(row=4,column=1,sticky='snew',ipadx=60,ipady=60)
    medium.config(command=lambda: mediumbutton())
    easy=Button(xo,text='Easy',bd=8, fg="black",font=('arial', 10,'bold'),bg="yellow")
    easy.grid(row=4,column=2,sticky='snew',ipadx=60,ipady=60)
    easy.config(command=lambda: easybutton()) """