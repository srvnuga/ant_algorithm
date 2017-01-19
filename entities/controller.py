from entities.board import Board


class Controller:
    __board = None
    __ant = None
    # todo add number of iteration

    def __init__(self, sizeOfBoard):
        # todo add init ant
        # todo init number of iteration
        self.__board = Board(sizeOfBoard)

    def start(self, max_number_of_iteration):
        # todo add logic for start process:
        # ant must be on start cell
        # controller must gte from board available cells and take them to ant
        # then controller get the answer from ant(id of cell which ant select)
        # and controller send this selected id to the board
        # it's required to use method process() until number of iteration < max_number_of_iteration

        pass

    def process(self):
        # todo logic for ONE iteration must be added here
        # in the end of process number of iteration must be +1
        pass

    def print(self):
        # todo add printing to console all information about board
        pass
