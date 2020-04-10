'''
Gabriel Ugolole. Sudoku solver v1 
'''
import SudokuBoard as sb


class Game(object):
    '''
    Class Game that defines game logic
    '''

    def __init__(self, boardfile):
        self.boardfile = boardfile
        self.puzzle = sb.BoardGame(boardfile).board #Stores the board game
    
    def start(self):
        self.game_over = False
        self._puzzle = [] #Stores a copy of the board  
        for i in range(sb.BOARD_SIZE):
            self._puzzle.append([]) 
            for j in range(sb.BOARD_SIZE):
                self._puzzle[i].append(self.puzzle[i][j])

    def check_win(self):
        # tranveses through the rows and cols to check for uniqueness
        for row in range(sb.BOARD_SIZE):
            if not self.__check_row(row):
                return False
        
        for col in range(sb.BOARD_SIZE):
            if not self.__check_column(col):
                return False
        
        #Checks each 3x3 square for uniqueness
        for row in range(sb.BOARD_SIZE//3):
            for col in range(sb.BOARD_SIZE//3):
                if not self.__check_square(row, col):
                    return False

        self.game_over = True
        return True


    def __check_board(self, block):
        return set(block) == set(range(1, 10))
    
    def __check_row(self, row):
        return self.__check_board(self._puzzle[row])
    
    def __check_column(self, col):
        return self.__check_board([self._puzzle[row][col] for row in range(sb.BOARD_SIZE)])

    def __check_square(self, row, col):
        return self.__check_board(
            [
                self._puzzle[r][c]
                for r in range(row*3, (row+1)*3)
                for c in range(col*3, (col+1)*3)
            ]
        )

"""
Main file that runs the game
"""
def draw(boardfile):
    pass
    
    