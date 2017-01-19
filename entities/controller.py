from entities.ant import Ant
from entities.board import Board


class Controller:
    __board = None
    __ant = None
    __iter_counter = None
    __max_iter_number = None

    def __init__(self, sizeOfBoard, max_number_of_iteration):
        self.__ant = Ant()
        self.__iter_counter = 0
        self.__max_iter_number = max_number_of_iteration
        self.__board = Board(sizeOfBoard * sizeOfBoard)

    def start(self, max_number_of_iteration):
        # todo add logic for start process:
        # ant must be on start cell
        # it's required to use method process() until number of iteration < max_number_of_iteration
        pass

    def start_iteration(self):
        pass

    def process(self):
        current_ant_id = self.__ant.
        pass

    def print(self):
        print("Iteration " + str(self.__iter_counter) + " of " + str(self.__max_iter_number))
        self.__board.print()