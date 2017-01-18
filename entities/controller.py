from entities.board import Board


class Controller:
    __board = None

    def __init__(self, sizeOfBoard):
        self.__board = Board(sizeOfBoard)
