#  IMPORTS------------------------------------------------------
import tkinter as tk
from tkinter.constants import INSERT
import winsound

# Create object------------------------------------------------
root = tk.Tk()

#Size of Window--------------------------------------------------
root.geometry("590x600")
root.resizable(0,0)
canvas = tk.Canvas(root)

#Title----------------------------------------------------------
root.title('Samoul_heng_G-10')


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
#Show when user Win!!!!!!----------------------------------
myWiner=tk.PhotoImage(file='images\youwin.png')

    #Show when user Loose!!!-----------------------------------
myLoser=tk.PhotoImage(file='images\gameover.png')

#winsound start Game------------------------
winsound.PlaySound("sound\start.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

#variable----------------------------------------------------
empty=0
wall=1
player=2
coin=3
monster=4
goal=5
Coins=0
Moving=23
NameOfGame=""
#--------------------------------------------------------
# Main VARIABLES
grid =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 3, 0, 3, 0, 1, 5, 0, 3, 0, 1],
    [1, 0, 1, 1, 4, 4, 0, 1, 1, 1, 0, 4, 1],
    [1, 3, 3, 4, 1, 4, 3, 1, 0, 1, 3, 3, 1],
    [1, 4, 4, 3, 1, 0, 0, 1, 0, 0, 0, 4, 1],
    [1, 3, 1, 0, 1, 3, 4, 1, 0, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 1],
    [1, 3, 1, 1, 1, 0, 0, 1, 3, 3, 4, 3, 1],
    [1, 4, 4, 3, 3, 3, 1, 1, 4, 3, 3, 3, 1],
    [1, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 
]

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
            x1 = (X * 45)
            y1 = (Y * 45)
            x2 = 45 + x1
            y2 = 45 + y1
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

#total and score--------------
    canvas.create_text(300,30,fill="yellow",font="Times 16  bold",text="Score: "+str(Coins))
    canvas.create_text(450,30,fill="yellow",font="Times 16  bold",text="Time Left: "+str(Moving))
    canvas.create_text(300,75,fill="yellow",font="Times 35  bold",text="Eat Coin!"+str(NameOfGame))
    return None

#to make player can move right , left , up , down----------
def gameOver():
    canvas.create_image(300,300,image=myLoser)
    gameOver()

def PositionOfPlayer(position) :
    global grid,Coins,Moving
    Moving+=(-1)
    isTrue=True
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row]==2 and position=="Right" and isTrue and grid[col][row +1]==0:
                grid[col][row]=0
                grid[col][row +1]=2
                isTrue=False
            if grid[col][row]==2 and position=="Left" and isTrue and grid[col][row -1]==0:
                grid[col][row]=0
                grid[col][row -1]=2
                isTrue=False
            if grid[col][row]==2 and position=="down" and isTrue and grid[col+1][row]==0:
                grid[col][row]=0
                grid[col+1][row]=2
                isTrue=False
            if grid[col][row]==2 and position=="Up" and isTrue and grid[col-1][row]==0:
                grid[col][row]=0
                grid[col-1][row]=2
                isTrue=False


            
            

    arrayToDrawing()

# #MoveRight-----------------------

def MoveRight(event):
    PositionOfPlayer("Right")


# #Move Left--------------------------------------
def MoveLeft(event):
      PositionOfPlayer("Left")

# #Move Down----------------------------------------------
def moveDown(event):
    PositionOfPlayer("down")

#Move Up-----------------------------------------------
def moveUp(event):
    PositionOfPlayer("Up")

#Key event of move Player----------------
root.bind("<Right>",MoveRight)#Right click    
root.bind("<Left>",MoveLeft)#Left click    
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)#Down clik

canvas.pack(expand=True, fill="both")

# Execute tkinter 
root.mainloop()