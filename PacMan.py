#################################################
# term project
#
# Your name: Justin Park
# Your andrew id: jjp2
#
#################################################

import math, copy, random

from cmu_112_graphics import *

#################################################

def appStarted(app):
    app.rows = gameDimensions()[0]
    app.cols = gameDimensions()[1]
    app.cellSize = gameDimensions()[2]
    app.margin = gameDimensions()[3]
    app.emptyColor = "black"
    app.outline = "blue"
    app.board = make2dList(app,app.rows,app.cols,app.emptyColor)
    app.pacManColor = "yellow"
    app.pacManOutline = "black"
    app.gameOver = False
    app.walls = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
                 [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
                 [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
                 [1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1],
                 [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
                 [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
                 [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
                 [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                 [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
                 [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
                 [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                 [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
                 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    app.wallColor = "blue"
    app.wallOutline = "blue"
    app.x = 0
    app.y = 0
    app.pillColor = "white"
    app.pillOutline = "black"
    app.pillSize = 7
    app.score = 0
    app.pills = make2dList(app,app.rows,app.cols,0)
    pacMan(app)
    
def make2dList(app,rows,cols,fill):
     return [([fill]*cols) for row in range(rows)]

def getCellCoords(app,row,col):
    cellWidth = ((app.width) - (2 * app.margin)) / app.cols
    cellHeight = ((app.height) - (2 * app.margin)) / app.rows
    x0 = app.margin + (cellWidth * col)
    y0 = app.margin + (cellHeight * row)
    x1 = app.margin + (cellWidth * (col + 1))
    y1 = app.margin + (cellHeight * (row + 1))
    return [x0,y0,x1,y1]

def drawCell(app,canvas,row,col,color,outlineColor):
    x0 = getCellCoords(app,row,col)[0]
    y0 = getCellCoords(app,row,col)[1]
    x1 = getCellCoords(app,row,col)[2]
    y1 = getCellCoords(app,row,col)[3]
    canvas.create_rectangle(x0, y0, x1, y1,fill=color,outline=outlineColor)

def drawCircle(app,canvas,row,col,color,outlineColor):
    x0 = getCellCoords(app,row,col)[0]
    y0 = getCellCoords(app,row,col)[1]
    x1 = getCellCoords(app,row,col)[2]
    y1 = getCellCoords(app,row,col)[3]
    canvas.create_oval(x0, y0, x1, y1,fill=color,outline=outlineColor)

def drawPill(app,canvas,row,col,color,outlineColor):
    x0 = getCellCoords(app,row,col)[0] + app.pillSize
    y0 = getCellCoords(app,row,col)[1] + app.pillSize
    x1 = getCellCoords(app,row,col)[2] - app.pillSize
    y1 = getCellCoords(app,row,col)[3] - app.pillSize
    canvas.create_rectangle(x0, y0, x1, y1,fill=color,outline=outlineColor)

def drawBoard(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app,canvas,row,col,app.board[row][col],app.outline)

def drawWalls(app,canvas):
    for i in range(len(app.walls)):
        for j in range(len(app.walls[0])):
            if app.walls[i][j] == 1:
                drawCell(app,canvas,i,j,app.wallColor,app.wallOutline)
                
def drawPacMan(app,canvas):
    drawCircle(app,canvas,app.pacManRow,app.pacManCol,app.pacManColor,
                                                            app.pacManOutline)

def drawPills(app,canvas):
    for i in range(len(app.board)):
        for j in range(len(app.board[0])):
            if app.walls[i][j] == 0:
                drawPill(app,canvas,i,j,app.pillColor,app.pillOutline)

def drawScore(app,canvas):
    canvas.create_text(app.width/2, app.height/30, text= f"Score: {app.score}",
                                    fill="white", font="Times 15 bold italic")

def drawGameOver(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="orange")
    canvas.create_text(app.width/2, app.height/2, text= "GAME OVER",
                                    fill="BLACK", font="Times 20 bold italic")

def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    drawBoard(app,canvas)
    drawWalls(app,canvas)
    drawPacMan(app,canvas)
    drawPills(app,canvas)
    drawScore(app,canvas)
    if app.gameOver:
        drawGameOver(app,canvas)

def pacMan(app):
    app.pacManRow = 11
    app.pacManCol = 9
    app.pacManRowPixel = (app.pacManRow * app.cellSize) + (app.cellSize / 2)
    app.pacManColPixel = (app.pacManCol * app.cellSize) + (app.cellSize / 2)

def pacManEats(app):
    if app.walls[app.pacManRow][app.pacManCol] == 0:
        app.walls[app.pacManRow][app.pacManCol] = 2
        app.score += 1

def gameOver(app):
    for i in range(len(app.board)):
        for j in range(len(app.board[0])):
            if app.walls[i][j] == 0:
                return False
    return True

def pacManLegal(app):
    if app.pacManCol >= app.cols:
        app.pacManCol = 0
    elif app.pacManCol < 0:
        app.pacManCol = app.cols - 1
    elif app.walls[app.pacManRow][app.pacManCol] == 1:
        return False
    return True

def movePacMan(app,drow,dcol):
    app.pacManRow += drow
    app.pacManCol += dcol
    if pacManLegal(app) == False:
        app.pacManRow -= drow
        app.pacManCol -= dcol
        return False
    pacManEats(app)
    if gameOver(app):
        app.gameOver = True
    return True

def keyPressed(app,event):
    if app.gameOver == False:
        if event.key == "Left" or event.key == "a":
            if app.x != -1:
                if movePacMan(app,0,-1):
                    app.x = -1
                    app.y = 0
        elif event.key == "Down" or event.key == "s":
            if app.y != 1:
                if movePacMan(app,1,0):
                    app.x = 0
                    app.y = 1
        elif event.key == "Right" or event.key == "d":
            if app.x != 1:
                if movePacMan(app,0,1):
                    app.x = 1
                    app.y = 0
        elif event.key == "Up" or event.key == "w":
            if app.y != -1:
                if movePacMan(app,-1,0): 
                    app.x = 0
                    app.y = -1

def timerFired(app):
    if app.gameOver == False:
        movePacMan(app,app.y,app.x)

def gameDimensions():
    rows = 21
    cols = 19
    cellSize = 20
    margin = 25
    return [rows,cols,cellSize,margin]

def playPacMan():
    rows = gameDimensions()[0]
    cols = gameDimensions()[1]
    cellSize = gameDimensions()[2]
    margin = gameDimensions()[3]
    width = (margin * 2) + (cellSize * cols)
    height = (margin * 2) + (cellSize * rows)
        
    runApp(width=width, height=height)

#################################################

def main():
    playPacMan()

if __name__ == '__main__':
    main()