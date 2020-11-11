## This is the main chess game engine that implements the rules of the game
## and stores the state of the the chess board, including its pieces and moves


class Game_state():
	
    def __init__(self):
        """
            The chess board is an 8 X 8 dimensional array (Matrix of 8 rows and 8 columns )
            i.e a list of lists. Each element of the Matrix is a string of two characters 
            representing the chess pieces in the order "type" + "colour"

            light pawn = pl
            dark pawn  = pd

            light knight = nl
            dark knight  = nd
            e.t.c

            empty board square = "  " ---> double empty space

        """

        self.board = [

            ["rd", "nd", "bd", "qd", "kd", "bd", "nd", "rd"],
            ["pd", "pd", "pd", "pd", "pd", "pd", "pd", "pd"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["pl", "pl", "pl", "pl", "pl", "pl", "pl", "pl"],
            ["rl", "nl", "bl", "ql", "kl", "bl", "nl", "rl"]]

        self.light_to_move = True # True = light's turn to play; False = dark's turn to play
        self.move_log = []        # keeps a log of all moves made withing a game
        self.move_piece = {"p":self.get_pawn_moves, "r":self.get_rook_moves, \
                        "q":self.get_queen_moves, "k":self.get_king_moves, \
                        "b":self.get_bishop_moves, "n":self.get_knight_moves}


    def get_pawn_moves(self, r, c, moves):
        """
            Calculates all possible pawn moves for a given color (light or dark)
            and appends them to a list

            input parameter(s):
            r     --> starting row (int)
            c     --> starting colum (int)
            moves --> possible moves container (list)

            return parameter(s):
            None
        """

        ## FIX
        if self.light_to_move: # if it's light's turn to move
            
            # if square is empty and in front of pawn and it is the pawn's first move
            if (r == 6) and (self.board[r-2][c] == "  "):
                moves.append(Move((r, c), (r-2, c), self.board)) # create a move object and append to list
            
            # if square is empty and in front of pawn
            if (r-1 >= 0) and (self.board[r-1][c] == "  "):
                moves.append(Move((r, c), (r-1, c), self.board)) # create a move object and append to list
            
            # if square on pawn's left diagonal has an opponent piece
            if ((r-1 >= 0) and (c-1 >= 0)) and (self.board[r-1][c-1][1] == "d"):
                moves.append(Move((r, c), (r-1, c-1), self.board)) # create a move object and append to list
            
            # if square on pawn's right diagonal has an opponent piece
            if ((r-1 >= 0) and (c+1 < len(self.board))) and (self.board[r-1][c+1][1] == "d"):
                moves.append(Move((r, c), (r-1, c+1), self.board)) # create a move object and append to list

        else: # if it's dark's turn to move
            
            # if square is empty and in front of pawn and it is the pawn's first move
            if (r == 1) and (self.board[r+2][c] == "  "):
                moves.append(Move((r, c), (r+2, c), self.board)) # create a move object and append to list
            
            # if square is empty and in front of pawn
            if (r+1 < len(self.board)) and (self.board[r+1][c] == "  "):
                moves.append(Move((r, c), (r+1, c), self.board)) # create a move object and append to list
            
            # if square on pawn's left diagonal has an opponent piece
            if ((r+1 < len(self.board)) and (c-1 >= 0)) and (self.board[r+1][c-1][1] == "l"):
                moves.append(Move((r, c), (r+1, c-1), self.board)) # create a move object and append to list
            
            # if square on pawn's right diagonal has an opponent piece
            if ((r+1 < len(self.board)) and (c+1 < len(self.board))) and (self.board[r+1][c+1][1] == "l"):
                moves.append(Move((r, c), (r+1, c+1), self.board)) # create a move object and append to list


    def get_bishop_moves(self, r, c, moves):
        
        """
            calculates all possible bishop moves for a given colour (light or dark)
            and appends them to a list

            input parameters:
            r     --> starting row (int)
            c     --> starting column (int)
            moves --> posiible moves container (list)

            return parameter(s):
            None
        """
        direction = ((-1, -1), (1, 1), (1, -1), (-1, 1))  # possible  Bishop direction
        if self.light_to_move:  # light piece turn to move
            for d in direction:
                for i in range(1, len(self.board)):
                    rownum = r + d[0] * i
                    colnum = c + d[1] * i
                    if (0 <= rownum < len(self.board)) and (
                            0 <= colnum < len(self.board)):  # making sure r and c on board
                        if self.board[rownum][colnum] == "  ":  # if square is empty
                            moves.append(Move((r, c), (rownum, colnum), (self.board)))
                        elif self.board[rownum][colnum][1] == "d":  # if square has opponent piece
                            moves.append(Move((r, c), (rownum, colnum), (self.board)))
                            break
                        else:
                            break  # when ally piece encountered
                    else:
                        break  # when off the board
        else:  # Dark piece turn to move
            for d in direction:
                for i in range(1, len(self.board)):
                    rownum = r + d[0] * i
                    colnum = c + d[1] * i
                    if (0 <= rownum < len(self.board)) and (
                            0 <= colnum < len(self.board)):  # making sure r and c on board
                        if self.board[rownum][colnum] == "  ":  # if square is empty
                            moves.append(Move((r, c), (rownum, colnum), (self.board)))
                        elif self.board[rownum][colnum][1] == "l":  # if square has opponent piece
                            moves.append(Move((r, c), (rownum, colnum), (self.board)))
                            break
                        else:
                            break  # when ally piece encountered
                    else:
                        break  # when off the board


    def get_knight_moves(self, r, c, moves):

        """
            calculates all possible knight moves for a given colour (light or dark)
            and appends them to a list

            input parameters:
            r     --> starting row (int)
            c     --> starting column (int)
            moves --> posiible moves container (list)

            return parameter(s):
            None
        """
        #possible squares for knight move
        squares = (
            (r+2,c+1), (r+2,c-1), (r-2,c+1), (r-2,c-1),
            (r+1,c+2), (r+1,c-2), (r-1,c+2), (r-1,c-2)
        )

        if self.light_to_move: # if it's light's turn to move
            available_squares = (" ", "d") #squares the knight can move to

            for square in squares:
                i,j = square
                if ( (0 <= i < len(self.board)) and (0 <= j < len(self.board))
                    and (self.board[i][j][1] in available_squares) ):

                    moves.append(Move((r, c), square, self.board)) # create a move object and append to list
        

        else: #if it's dark's turn to move
            available_squares = (" ", "l") #squares the knight can move to

            for square in squares:
                i,j = square
                if ( (0 <= i < len(self.board)) and (0 <= j < len(self.board))
                    and (self.board[i][j][1] in available_squares) ):

                    moves.append(Move((r, c), square, self.board)) # create a move object and append to list


    def get_king_moves(self, r, c, moves):
        """
            calculates all possible king moves for a given colour (light or dark)
            and appends them to a list

            input parameters:
            r     --> starting row (int)
            c     --> starting column (int)
            moves --> posiible moves container (list)

            return parameter(s):
            None
        """

        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        enemy_color = "d" if self.light_to_move else "l"

        for d in directions:
            end_row = r + d[0]
            end_col = c + d[1]

            if 0 <= end_row < 8 and 0<= end_col < 8:
                destination = self.board[end_row][end_col]
                if destination[1] == enemy_color or destination == "  ":
                    moves.append(Move((r, c), (end_row, end_col), self.board))

            

    def get_rook_moves(self, r, c, moves):
        """
            calculates all possible rook moves for a given colour (light or dark)
            and appends them to a list

            input parameters:
            r     --> starting row (int)
            c     --> starting column (int)
            moves --> posiible moves container (list)

            return parameter(s):
            None
         """
        direction = (-1, 1) # possible direction

        if self.light_to_move: # if it's light's turn to move

            for d in direction:
                #rows
                for i in range(1,len(self.board)):
                    rownum = r + d*i
                    if (0 <= rownum < len(self.board)): # making sure row is on board
                        if self.board[rownum][c] == "  ": # if square is empty
                            moves.append(Move((r,c), (rownum,c), (self.board)))
                        elif self.board[rownum][c][1] == "d": # if square has opponent piece
                            moves.append(Move((r,c), (rownum,c), (self.board)))
                            break
                        else:
                            break # when ally piece encountered
                    else:
                        break # when off the board
                #columns
                for i in range(1,len(self.board)):
                    colnum = c + d*i
                    if (0 <= colnum < len(self.board)): # making sure column is on board
                        if self.board[r][colnum] == "  ": # if square is empty
                            moves.append(Move((r,c), (r,colnum), (self.board)))
                        elif self.board[r][colnum][1] == "d": # if square has opponent piece
                            moves.append(Move((r,c), (r,colnum), (self.board)))
                            break
                        else:
                            break # when ally piece encountered
                    else:
                        break # when off the board

         #if it's dark's turn to move
        else:
            for d in direction:
                #rows
                for i in range(1,len(self.board)):
                    rownum = r + d*i
                    if (0 <= rownum < len(self.board)): # making sure row is on board
                        if self.board[rownum][c] == "  ": # if square is empty
                            moves.append(Move((r,c), (rownum,c), (self.board)))
                        elif self.board[rownum][c][1] == "l": # if square has opponent piece
                            moves.append(Move((r,c), (rownum,c), (self.board)))
                            break
                        else:
                            break # when ally piece encountered
                    else:
                        break # when off the board
                #columns
                for i in range(1,len(self.board)):
                    colnum = c + d*i
                    if (0 <= colnum < len(self.board)): # making sure column is on board
                        if self.board[r][colnum] == "  ": # if square is empty
                            moves.append(Move((r,c), (r,colnum), (self.board)))
                        elif self.board[r][colnum][1] == "l": # if square has opponent piece
                            moves.append(Move((r,c), (r,colnum), (self.board)))
                            break
                        else:
                            break # when ally piece encountered
                    else:
                        break # when off the board


    def get_queen_moves(self, r, c, moves):
        """
        Calculates all possible queen moves for a given color (light or dark)
        based on bishop and rook moves.

        input parameter(s):
        r     --> starting row (int)
        c     --> starting colum (int)
        moves --> possible moves container (list)

        return parameter(s):
        None
        """
        ##TODO
        self.get_bishop_moves(r, c, moves)
        self.get_rook_moves(r, c, moves)


    def make_move(self, move):
        """
            moves pieces on the board
        """
        self.board[move.start_row][move.start_col] = "  "
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move) # log move
        self.light_to_move = not self.light_to_move # next player to move

        # Pawn Promotion
        if move.ispawn_promotion:
            promoted_piece = input("Input q(Queen),r(rook),b(bishop) or n(knight) to promote ") #we can add this to the ui later
            promotion_options = ("q","r","b","n")
            if promoted_piece in promotion_options:
                self.board[move.end_row][move.end_col] = promoted_piece + move.piece_moved[1]
                #creates a default queen promotion if wrong input is given
            else:
                self.board[move.end_row][move.end_col] = "q" + move.piece_moved[1]

    def undo_move(self, look_ahead_mode = False):
        """
            undoes last move
        """
        if self.move_log:
            last_move = self.move_log.pop()
            self.board[last_move.start_row][last_move.start_col] = last_move.piece_moved
            self.board[last_move.end_row][last_move.end_col] = last_move.piece_captured
            self.light_to_move = not self.light_to_move

            print("undoing ->", last_move.get_chess_notation())
        else:
            print("All undone!")


    def get_valid_moves(self):
        return self.get_possible_moves()


    def get_possible_moves(self):

        moves = []

        turn = "l" if self.light_to_move else "d"

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][1] == turn:
                    self.move_piece[self.board[i][j][0]](i, j, moves)

        return moves, turn



class Move():

    # map ranks to rows
    ranks_to_rows = {"1":7, "2":6, "3":5, "4":4,
                    "5":3, "6":2, "7":1, "8":0}

    # map rows to ranks (revers of ranks to rows)
    rows_to_ranks = {row:rank for rank, row in ranks_to_rows.items()}

    # map files to columns
    files_to_cols = {"a":0, "b":1, "c":2, "d":3,
                    "e":4, "f":5, "g":6, "h":7}

    # map columns to files (revers of files to columns)
    cols_to_files = {col:file for file, col in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        """
            A Move class abstracting all parameters needed
            for moving chess pieces on the board

            input parameter(s):
            start_sq --> (row, column) of piece to be moved (tuple)
            end_square --> (row, column) of move destination on the board (tuple)
            board --> board object referencing current state of the board (class Game_state)
        """
        self.start_row = start_sq[0] # row location of piece to be moved
        self.start_col = start_sq[1] # column location of piece to be moved
        self.end_row = end_sq[0] # intended row destination of piece to be moved
        self.end_col = end_sq[1] # intended column destiantion of piece to e moved
        self.piece_moved = board[self.start_row][self.start_col] # actual piece moved
        self.piece_captured = board[self.end_row][self.end_col] # opponent piece if any on the destination square
        self.ispawn_promotion = False
        if (self.piece_moved == "pl" and self.end_row == 0) or (self.piece_moved == "pd" and self.end_row == 7):
            self.ispawn_promotion = True

    def get_chess_notation(self):
        """
            creates a live commentary of pieces moved on the chess board during a game

            input parameter(s):
            None

            return parameter(s)
            commentary (string)
        """
        return self.piece_moved[0].upper() + "(" + self.get_rank_file(self.start_row, self.start_col) + ") to " + self.get_rank_file(self.end_row, self.end_col) + \
            "(" + self.piece_captured[0].upper() + " captured!)" if self.piece_captured != "  " else self.piece_moved[0].upper() + "(" + self.get_rank_file(self.start_row, self.start_col) + ") to " + \
            self.get_rank_file(self.end_row, self.end_col)


    def get_rank_file(self, r, c):
        """
            calls cols_to_file and rows_to_rank attributes

            input parameter(s):
            r --> row to be converted to rank (int)
            c --> column to be converted to file (int)

            return parameter(s):
            "file" + "rank" (str)
        """
        return self.cols_to_files[c] + self.rows_to_ranks[r]


    def __eq__(self, other):
        """
            operator overloading for equating two move objects
        """

        if isinstance(other, Move): # if first (self) and second (other) parameters are both Move objects
            return self.start_row == other.start_row and self.start_col == other.start_col and \
                    self.end_row == other.end_row and self.end_col == other.end_col
        else:
            return False


    def __ne__(self, other):
        """
            "not equals to" --> conventional counterpart to __eq__
        """
        return self.__eq__(other)


    def __str__(self):
        """
            operator overloading for printing Move objects
        """
        return "({}, {}) ({}, {})".format(self.start_row, self.start_col, self.end_row, self.end_col)


