from entities.ant import Ant
from entities.board import Board


class Controller:
    __board = None
    __ant = None
    __iter_counter = None

    def __init__(self, sizeOfBoard):
        self.__ant = Ant()
        self.__iter_counter = 0
        self.__board = Board(sizeOfBoard)

    def start(self, max_number_of_iteration):
        # todo add logic for start process:
        # ant must be on start cell
        # it's required to use method process() until number of iteration < max_number_of_iteration
        pass

    def init_iteration(self):
       pass

    def process(self):
        # todo logic for ONE iteration must be added here:
        # controller must get from board available cells and take them to ant
        # then controller get the answer from ant(id of cell which was selected by ant)
        # and controller send this selected id to the board
        # in the end of process number of iteration must be +1
        pass

    def print(self):
        # todo add printing to console all information about board
        pass
