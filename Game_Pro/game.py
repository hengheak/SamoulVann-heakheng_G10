#  IMPORTS------------------------------------------------------
import tkinter as tk
import winsound
# from typing import Generator
from tkinter import messagebox
#  MAIN Code-----------------------------------------------------
root = tk.Tk()

#Size of Window--------------------------------------------------
root.geometry("600x600")
root.resizable(0,0)
canvas = tk.Canvas(root)

#Title----------------------------------------------------------
root.title('Samoul_G-10')


#add image

        #Player-------------------------------------------------
myImage= tk.PhotoImage(file='images\player.png')
        # Coin---------------------------------------------------
myCoin=tk.PhotoImage(file='images\coin.png')
        #Monster-----------------------------------------------
myEnemy=tk.PhotoImage(file='images\monster.png')
        #Flag---------------------------------------------------
myGoal=tk.PhotoImage(file='images\Cflage.png')
        #Wall---------------------------------------------------
myWall=tk.PhotoImage(file='images\wall.png')
        #Background---------------------------------------------
myBackground=tk.PhotoImage(file='images\gBackg.png')


#Image Result 
    #
    #
    #
    #Show when user Win!!!!!!----------------------------------
myWiner=tk.PhotoImage(file='images\youwin.png')

    #Show when user Loose!!!-----------------------------------
myLoser=tk.PhotoImage(file='images\gameover.png')


#Note----------------------------------------------------
empty=0
wall=1
player=2
coin=3
monster=4
goal=5
#--------------------------------------------------------

#winsound
winsound.PlaySound("sound\start.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
# Main VARIABLES
grid =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 3, 0, 3, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 4, 0, 1, 1, 1, 0, 0, 1],
    [1, 3, 4, 1, 4, 3, 1, 0, 1, 0, 0, 1],
    [1, 4, 3, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 3, 4, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 3, 4, 3, 1],
    [1, 4, 3, 3, 3, 1, 1, 0, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 
]
Coins=0
Moving=23
NameOfGame=""

#Create background-------------------------------
def bgOfbackround():
    global myBackground
    canvas.create_image(400,400,image=myImage)
    canvas.create_image(100,100,image=myBackground)
bgOfbackround()

#Create button------------------------------------
def button():
    arrayToDrawing()
buttonPlay=tk.Button(text="Play Games",font=("Time",20,"bold"),bg="#FF8C00",padx=12,pady=5,command=button)
canvas.create_window(300,300,window=buttonPlay)


#  FUNCTION
def arrayToDrawing():
    global myImage,myCoin,Moving
    canvas.delete("all")
    #Add background Image and Images instead grid colors
    canvas.create_image(210,310, image=myBackground)
    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 50)
            y1 = (Y * 50)
            x2 = 50 + x1
            y2 = 50 + y1
            value = grid[Y][X]
            if value != player:
                if value !=coin:
                    if value!=monster:
                        if value !=goal:
                            if value==wall:
                                canvas.create_image(x1+26,y1+27,image=myWall)
                        else:
                            canvas.create_image(x1+26,y1+27,image=myGoal)
                    else:
                        canvas.create_image(x1+26,y1+27,image=myEnemy)
                else:
                    canvas.create_image(x1+26,y1+27,image=myCoin)
            else:
                canvas.create_image(x1+23,y1+27,image=myImage)

    canvas.create_text(350,30,fill="yellow",font="Times 16  bold",text="Score: "+str(Coins))
    canvas.create_text(500,30,fill="yellow",font="Times 16  bold",text="Time Left: "+str(Moving))
    canvas.create_text(300,75,fill="yellow",font="Times 35  bold",text="Eat Coin!"+str(NameOfGame))
    return None

#MoveRight------------------------
def PositionOfPlayer(grid) :
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row]== 2:
                position=[column,row]
    return position

def MoveRight(event):
    global grid, Coins,Moving
    Moving=Moving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    oldValue = 0
    if grid[playerrow][playercolumn +1]!=1:
        grid[playerrow][playercolumn ]=0
        oldValue = grid[playerrow][playercolumn+1]
        grid[playerrow][playercolumn +1]=2
    
    if oldValue==coin:
        winsound .PlaySound('sound\coin.wav', winsound.SND_FILENAME)
        Coins=Coins+10
    arrayToDrawing() 
    if oldValue==monster:
        winsound.PlaySound("sound\lost.wav",winsound.SND_FILENAME)
               



#Move Left--------------------------------------
def MoveLeft(event):
    global grid, Coins,Moving
    Moving=Moving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    oldValue = 0
    if grid[playerrow][playercolumn -1]!=1:
        grid[playerrow][playercolumn ]=0
        oldValue = grid[playerrow][playercolumn-1]
        grid[playerrow][playercolumn -1]=2
    
    if oldValue==coin:
        winsound .PlaySound('sound\coin.wav', winsound.SND_FILENAME)
        Coins=Coins+10
    arrayToDrawing() 
    if oldValue==monster:
        winsound.PlaySound("sound\lost.wav",winsound.SND_FILENAME)

#Move Down----------------------------------------------
def moveDown(event):
    global grid
    stoped=False
    for row in range(len(grid)):
        for coml in range(len(grid[row])):
            if grid[row][coml]==2 and not stoped and grid[row+1][coml]!=1 :
                grid[row][coml]=0
                grid[row+1][coml]=2
                stoped=True
    print(grid)
    arrayToDrawing()


#Move Up-----------------------------------------------
def moveUp(event):
    global grid
    stoped=False
    for row in range(len(grid)):
        for coml in range(len(grid[row])):
            if grid[row][coml]==2 and grid[row-1][coml]!=1:
                grid[row][coml]=0
                grid[row-1][coml]=2
                stoped=True
    print(grid)
    arrayToDrawing()

root.bind("<Right>",MoveRight)#Right click    
root.bind("<Left>",MoveLeft)#Left click    
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)#Down clik
canvas.pack(expand=True, fill="both")

root.mainloop()