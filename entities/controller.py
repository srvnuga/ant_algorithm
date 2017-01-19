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

    def start(self):
        start_id = self.__board.get_start_cell_id()
        finish_id = self.__board.get_finish_cell_id()
        while self.__iter_counter < self.__max_iter_number:
            self.__board.randomize_cells()
            self.__ant.move(start_id)
            while True:
                current_ant_cell = self.__ant.get_current_cell()
                if current_ant_cell == finish_id:
                    break
                old_ant_cell = self.__ant.get_old_cell()
                available_cells = self.__board.get_available_cells_by_id(current_ant_cell, old_ant_cell)
                selected_ant_cell = self.__ant.get_selected_cell(available_cells)
                selected_ant_cell.increase_counter()
            self.__iter_counter += 1
            self.print()

    def print(self):
        print("Iteration " + str(self.__iter_counter) + " of " + str(self.__max_iter_number))
        self.__board.print()