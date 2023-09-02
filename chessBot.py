import copy
import itertools
from itertools import chain

board = [["R", "P", "0", "0", "0", "0", "p", "r"], ["N", "P", "0", "0", "0", "0", "p", "n"],
         ["B", "P", "0", "0", "0", "0", "p", "b"], ["Q", "P", "0", "0", "0", "0", "p", "q"],
         ["K", "P", "0", "0", "0", "0", "p", "k"], ["B", "P", "0", "0", "0", "0", "p", "b"],
         ["N", "P", "0", "0", "0", "0", "p", "n"], ["R", "P", "0", "0", "0", "0", "p", "r"]]


def printBoard(board):
    num = 7
    while num >= 0:
        for column in board:
            print(column[num], end="|")
        print("")
        num -= 1

dictionary = {
    "a1":(0,0),
    
}

dict = {
    "a1": (0, 0),
    "a2": (0, 1),
    "a3": (0, 2),
    "a4" : (0, 3),
    "a5" : (0, 4),
    "a6" : (0, 5),
    "a7" :(0, 6),
    "a8" : (0, 7),
    
    "b1" : (1, 0),
    "b2" : (1, 1),
    "b3" : (1, 2),
    "b4" : (1, 3),
    "b5" : (1, 4),
    "b6" : (1, 5),
    "b7" : (1, 6),
    "b8" : (1, 7),
    
    "c1" : (2, 0),
    "c2" : (2, 1),
    "c3" : (2, 2),
    "c4" : (2, 3),
    "c5" : (2, 4),
    "c6" : (2, 5),
    "c7" : (2, 6),
    "c8" : (2, 7),
    
    "d1" : (3, 0),
    "d2" : (3, 1),
    "d3" : (3, 2),
    "d4" : (3, 3),
    "d5" : (3, 4),
    "d6" : (3, 5),
    "d7" : (3, 6),
    "d8" : (3, 7),
    
    "e1" : (4, 0),
    "e2" : (4, 1),
    "e3" : (4, 2),
    "e4" : (4, 3),
    "e5" : (4, 4),
    "e6" : (4, 5),
    "e7" : (4, 6),
    "e8" : (4, 7),

    "f1" : (5, 0),
    "f2" : (5, 1),
    "f3" : (5, 2),
    "f4" : (5, 3),
    "f5" : (5, 4),
    "f6" : (5, 5),
    "f7" : (5, 6),
    "f8" : (5, 7),
    
    "g1" : (6, 0),
    "g2" : (6, 1),
    "g3" : (6, 2),
    "g4" : (6, 3),
    "g5" : (6, 4),
    "g6" : (6, 5),
    "g7" : (6, 6),
    "g8" : (6, 7),
    
    "h1" : (7, 0),
    "h2" : (7, 1),
    "h3" : (7, 2),
    "h4" : (7, 3),
    "h5" : (7, 4),
    "h6" : (7, 5),
    "h7" : (7, 6),
    "h8" : (7, 7)
}
def updateMoveSet(moveSet):
    for move in moveSet:
        if move[2]:
            move[0]+=1
        else:
            move[0]-=1
        if move[3]:
            move[1]+=1
        else:
            move[1]-=1

def getValidMoves(square,board):
    x = square[0]
    y = square[1]
    piece = board[x][y]
    finalMoves = []
    def getWhitePawnMoves():
        moves=[]
        if board[x][y + 1] == "0":
            moves.append((x, y + 1))
            if y == 1:
                if board[x][y + 2] == "0":
                    moves.append((x, y + 2))
        try:
            if board[x - 1][y + 1].islower():
                moves.append((x - 1, y + 1))
        except:
            pass
        try:
            if board[x + 1][y + 1].islower():
                moves.append((x + 1, y + 1))
        except:
            pass
        return moves

    def getBlackPawnMoves():
        moves = []
        if board[x][y - 1] == "0":
            moves.append((x, y - 1))
            if y == 6:
                if board[x][y - 2] == "0":
                    moves.append((x, y - 2))
        try:
            if board[x - 1][y - 1].islower():
                moves.append((x - 1, y - 1))
        except:
            pass
        try:
            if board[x + 1][y - 1].islower():
                moves.append((x + 1, y - 1))
        except:
            pass
        return moves

    def getKnightMoves():
        moves = []
        moves.append((x + 1, y + 2))
        moves.append((x + 1, y - 2))
        moves.append((x - 1, y + 2))
        moves.append((x - 1, y - 2))
        moves.append((x + 2, y + 1))
        moves.append((x + 2, y - 1))
        moves.append((x - 2, y + 1))
        moves.append((x - 2, y - 1))


        validMoves = []
        for move in moves:
            if not (((move[0] < 0) or (move[0] > 7)) or ((move[1] < 0) or (move[1] > 7))):
                validMoves.append(move)

        moves = []
        if piece.islower():
            for move in validMoves:
                if not board[move[0]][move[1]].islower():
                    moves.append(move)
        else:
            for move in validMoves:
                if not board[move[0]][move[1]].isupper():
                    moves.append(move)

        return moves

    def getRookMoves():
        i = 1
        moves=[]
        moveSet = [[x, y, True, True], [x, y, True, False], [x, y, False, True], [x, y, False, False]]
        while i<=8:
            for move in moveSet:
                if move[2]:
                    if move[3]:
                        move[0]+=1
                    else:
                        move[0]-=1
                else:
                    if move[3]:
                        move[1]+=1
                    else:
                        move[1]-=1
            toBeRemoved = []
            for move in moveSet:
                if move[0]<0 or move[0]>7 or move[1]<0 or move[1]>7:
                    toBeRemoved.append(move)
                    continue

                target = board[move[0]][move[1]]
                if target == "0":
                    moves.append((move[0],move[1]))
                    continue
                if piece.islower():
                    if target.isupper():
                        moves.append((move[0],move[1]))
                    toBeRemoved.append(move)
                else:
                    if target.islower():
                        moves.append((move[0],move[1]))
                    toBeRemoved.append(move)
            for move in toBeRemoved:
                moveSet.remove(move)
            i+=1
        return moves

    def getBishopMoves():
        moves = []
        i=1
        moveSet = [[x,y, True, True], [x,y, True, False], [x,y, False, True], [x, y,False,False]]
        while (i <= 8):
            for move in moveSet:
                if move[2]:
                    move[0] += 1
                else:
                    move[0] -= 1
                if move[3]:
                    move[1] += 1
                else:
                    move[1] -= 1
            toBeRemoved = []
            for move in moveSet:
                if move[0]<0 or move[0]>7 or move[1]<0 or move[1]>7:
                    toBeRemoved.append(move)
                    continue
                target = board[move[0]][move[1]]
                if target == "0":
                    moves.append((move[0],move[1]))
                    continue
                if piece.islower():
                    if target.isupper():
                        moves.append((move[0],move[1]))
                    toBeRemoved.append(move)
                else:
                    if target.islower():
                        moves.append((move[0],move[1]))
                    toBeRemoved.append(move)
            for move in toBeRemoved:
                moveSet.remove(move)
            i+=1
        return moves

    def getQueenMoves():
        moves = getBishopMoves()
        moves.extend(getRookMoves())
        return moves
    def getKingMoves():
        moves = [[x,y+1],[x,y-1],[x+1,y],[x-1,y],[x+1,y+1],[x+1,y-1],[x-1,y+1],[x-1,y-1]]
        toBeRemoved = []
        for move in moves:
            if move[0]<0 or move[0]>7 or move[1]<0 or move[1]>7:
                toBeRemoved.append(move)
        for move in toBeRemoved:
            moves.remove(move)
        toBeRemoved = []
        for move in moves:
            target = board[move[0]][move[1]]
            if piece.islower():
                if target.islower():
                    toBeRemoved.append(move)
            else:
                if target.isupper():
                    toBeRemoved.append(move)
        for move in toBeRemoved:
            moves.remove(move)
        return moves

    if piece=="p":
        return getBlackPawnMoves()
    if piece=="P":
        return getWhitePawnMoves()
    if piece=="R" or piece == "r":
        return getRookMoves()
    if piece=="N" or piece=="n":
        return getKnightMoves()
    if piece =="B" or piece =="b":
        return getBishopMoves()
    if piece =="Q" or piece=="q":
        return getQueenMoves()
    if piece =="K" or piece =="k":
        return getKingMoves()

def allLegalMoves(board,isWhite):
    allMoves = []
    i = 0
    for row in board:
        j=0
        for piece in row:
            if (piece.islower() ^ isWhite) and piece != '0':
                moves = getValidMoves((i,j),board)
                for move in moves:
                    newBoard = makeMove(board,piece,(i,j),move)
                    if not isInCheck(isWhite,board):
                        allMoves.append(move)
            j+=1
        i+=1

    return allMoves



def changeGameState(board, depth, isWhite):
        if depth == 0:
            return board
        stateArray = []
        i = 0
        for row in board:
            j = 0
            for piece in row:
                if  (piece.islower() ^ isWhite) and piece != '0':

                    moves = getValidMoves((i,j),board)
                    for move in moves:
                        newBoard = makeMove(board,piece,(i,j),move)
                        if not isInCheck(isWhite,newBoard):
                            stateArray.append(changeGameState(newBoard,depth-1,not isWhite))


                j+=1
            i+=1

        if stateArray==[]:
            return board
        scores = []
        for state in stateArray:
            scores.append(evaluationFunction(newBoard))
        if isWhite:
            return stateArray[scores.index(max(scores))]
        else:
            return stateArray[scores.index(min(scores))]

def makeMove(board,piece,oldPos,newPos):
    newBoard = [0,0,0,0,0,0,0,0]
    i = 0
    for column in board:
        newBoard[i] = column[:]
        i+=1
    newBoard[newPos[0]][newPos[1]] = piece
    newBoard[oldPos[0]][oldPos[1]] = "0"
    return newBoard






def evaluationFunction(board):
    evaluation = 0





    for row in board:
        for piece in row:
            if piece == "Q":
                evaluation+=9
            if piece =="q":
                evaluation-=9
            if piece =="R":
                evaluation+=5
            if piece =="r":
                evaluation-=5
            if piece == "B" or piece=="N":
                evaluation+=3
            if piece == "b" or piece == "n":
                evaluation-=3
            if piece =="P":
                evaluation+=1
            if piece =="p":
                evaluation-=1
    if allLegalMoves(board,True) == []:
        return -100

    if allLegalMoves(board,False)==[]:
        return 100


    return evaluation



def isInCheck(isWhite,board):

    kingPos = 0
    i=0
    for column in board:
        j=0
        for piece in column:
            if isWhite:
                if piece=="K":
                    kingPos = (i,j)
            else:
                if piece=="k":
                    kingPos = (i,j)
            j+=1
        i+=1
    i = 0
    for column in board:
        j = 0
        for piece in column:
            if (isWhite and piece.islower()) or (not isWhite and piece.isupper()):
                for move in getValidMoves((i,j),board):
                    if move==kingPos:
                        return True

            j+=1
        i+=1
    return False







def runGame(isPlayerWhite):
    newBoard = board
    if isPlayerWhite:
        printBoard(newBoard)
        fromSquare = dict[input("Select square to move from:\n")]
        toSquare = dict[input("Select square to move from:\n")]
        newBoard = makeMove(newBoard,newBoard[fromSquare[0]][fromSquare[1]],fromSquare,toSquare)
        printBoard(newBoard)
        newBoard = changeGameState(board,5,False)
        printBoard(newBoard)
    else:
        newBoard = changeGameState(newBoard,4,True)
        printBoard(newBoard)
runGame(False)




