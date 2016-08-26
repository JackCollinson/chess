class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s%d: %s %s" % (self.x, self.y, self.color, self.name)

class WhitePawn(Piece):
    color = "White"
    name = "Pawn"
    code = 'p'
    moveset = [(0,1),(0,2),(1,1),(-1,1)]

class BlackPawn(Piece):
    color = "Black"
    name = "Pawn"
    code = 'P'
    moveset = [(0,-1),(0,-2),(1,-1),(-1,-1)]

class WhiteKnight(Piece):
    color = "White"
    name = "Knight"
    code = 'n'
    moveset = [(1,2),(2,1),(-1,2),(-2,1),
                (-1,-2),(-2,-1),(1,-2),(2,-1)]


class BlackKnight(Piece):
    color = "Black"
    name = "Knight"
    code = 'N'
    moveset = [(1,2),(2,1),(-1,2),(-2,1),
                (-1,-2),(-2,-1),(1,-2),(2,-1)]

class WhiteBishop(Piece):
    color = "White"
    name = "Bishop"
    code = 'b'
    moveset = []
    for i in range(1,8):
        moveset.append((i,i))
        moveset.append((-i,i))
        moveset.append((i,-i))
        moveset.append((-i,-i))

class BlackBishop(Piece):
    color = "Black"
    name = "Bishop"
    code = 'B'
    moveset = []
    for i in range(1,8):
        moveset.append((i,i))
        moveset.append((-i,i))
        moveset.append((i,-i))
        moveset.append((-i,-i))

class WhiteRook(Piece):
    color = "White"
    name = "Rook"
    code = 'r'
    moveset = []
    for i in range(1,8):
        moveset.append((0,i))
        moveset.append((0,-i))
        moveset.append((i,0))
        moveset.append((-i,0))

class BlackRook(Piece):
    color = "Black"
    name = "Rook"
    code = 'R'
    moveset = []
    for i in range(1,8):
        moveset.append((0,i))
        moveset.append((0,-i))
        moveset.append((i,0))
        moveset.append((-i,0))

class WhiteQueen(Piece):
    color = "White"
    name = "Queen"
    code = 'q'
    moveset = []
    for i in range(1,8):
        moveset.append((i,i))
        moveset.append((-i,i))
        moveset.append((i,-i))
        moveset.append((-i,-i))
        moveset.append((0,i))
        moveset.append((0,-i))
        moveset.append((i,0))
        moveset.append((-i,0))

class BlackQueen(Piece):
    color = "Black"
    name = "Queen"
    code = 'Q'
    moveset = []
    for i in range(1,8):
        moveset.append((i,i))
        moveset.append((-i,i))
        moveset.append((i,-i))
        moveset.append((-i,-i))
        moveset.append((0,i))
        moveset.append((0,-i))
        moveset.append((i,0))
        moveset.append((-i,0))


class WhiteKing(Piece):
    color = "White"
    name = "King"
    code = 'k'
    moveset = [(0,1),(1,1),(1,0),(1,-1),
                (0,-1),(-1,-1),(-1,0),(-1,1)]

class BlackKing(Piece):
    color = "Black"
    name = "King"
    code = 'K'
    moveset = [(0,1),(1,1),(1,0),(1,-1),
                (0,-1),(-1,-1),(-1,0),(-1,1)]

def letterToNumber(letter):
    return ord(letter) - 64

def numberToLetter(number):
    return chr(number + 64)

def moveAvailable(piece, moveFrom, moveTo):
    fromX = letterToNumber(moveFrom[0])
    fromY = letterToNumber(moveFrom[1]) + 16
    toX = letterToNumber(moveTo[0])
    toY = letterToNumber(moveTo[1]) + 16
    return (toX - fromX, toY - fromY) in piece.moveset


class Board:
    pieces = {}

    # sets pieces for default chessboard
    def setChessboard(self):
        # white pieces
        self.pieces['A1'] = WhiteRook('A',1)
        self.pieces['B1'] = WhiteKnight('B',1)
        self.pieces['C1'] = WhiteBishop('C',1)
        self.pieces['D1'] = WhiteQueen('D',1)
        self.pieces['E1'] = WhiteKing('E',1)
        self.pieces['F1'] = WhiteBishop('F',1)
        self.pieces['G1'] = WhiteKnight('G',1)
        self.pieces['H1'] = WhiteRook('H',1)

        # white pawns
        for i in range(8):
            piece = WhitePawn(numberToLetter(i+1),2)
            key = "%s2" % numberToLetter(i+1)
            self.pieces[key] = piece

        # black pawns
        for i in range(8):
            piece = BlackPawn(numberToLetter(i+1),7)
            key = "%s7" % numberToLetter(i+1)
            self.pieces[key] = piece

        # black pieces
        self.pieces['A8'] = BlackRook('A',8)
        self.pieces['B8'] = BlackKnight('B',8)
        self.pieces['C8'] = BlackBishop('C',8)
        self.pieces['D8'] = BlackQueen('D',8)
        self.pieces['E8'] = BlackKing('E',8)
        self.pieces['F8'] = BlackBishop('F',8)
        self.pieces['G8'] = BlackKnight('G',8)
        self.pieces['H8'] = BlackRook('H',8)

    def move(self, piece, moveFrom, moveTo):
        if moveFrom in self.pieces:
            if moveAvailable(piece, moveFrom, moveTo):
                piece = self.pieces.get(moveFrom)
                self.pieces[moveTo] = piece
                del self.pieces[moveFrom]
            else:
                print "error: move not available"
        else:
            print "error: no piece at given position"


    # prints board to console, using code values for each piece
    def __str__(self):
        board = ""
        for y in range(8,0,-1):
            board += str(y) + " "
            for x in range(1,9):
                key = "%s%d" % (numberToLetter(x), y)
                if self.pieces.has_key(key):
                    board += "[%s]" % (self.pieces.get(key).code)
                else:
                    board += "[ ]"
            board += "\n"
        board += "   A  B  C  D  E  F  G  H"
        return board


chessboard = Board()
chessboard.setChessboard()
print(chessboard)

while(True):
    moveFrom = raw_input("Move: ").upper()
    moveTo = raw_input("To: ").upper()
    chessboard.move(chessboard.pieces.get(moveFrom), moveFrom, moveTo)
    print(chessboard)
