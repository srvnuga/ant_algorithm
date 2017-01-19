from entities.cell import Cell
from entities.cells_group import CellsGroup
import random
import math


class Board:
    __cells = None  # list of cells
    __cells_coords = None  # 2 dimension map to connect Id of cells With X,Y coords

    def __init__(self, size):
        self.cells_coords = CellsGroup()
        self.create_board(size)
        self.randomize_cells()
        self.refresh_mapping(self.__cells)

    def create_board(self, size):
        self.__cells = []
        if size <= 0:
            raise TypeError("Size can't be < 0")
        for cellid in range(0, size):
            c = Cell(cellid)
            self.__cells.append(c)

    def refresh_mapping(self, list_cells):
        if not isinstance(list_cells, list):
            raise TypeError("list_cells is not a list!")
        self.cells_coords.create_mapping(list_cells)

    def randomize_cells(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            for cell in self.__cells:
                c = random.randrange(1, 10, 1)
                b = random.randrange(1, 10, 1)
                feromon = c + b * 0.1
                cell.set_feromon(feromon)

    def set_start_cell(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            self.__cells[0].set_cell_state(1)

    def set_finish_cell(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            self.__cells[0].set_cell_state(2)

    def get_start_cell(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        for cell in self.__cells:
            if cell.is_start():
                return cell

    def get_cell_by_id(self, cell_id):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return None
        else:
            for cell in self.__cells:
                if cell.get_id() == cell_id:
                    return cell
            raise TypeError("Can not find cell with id = %d" % cell_id)

    def get_cells_by_ids(self, list_of_ids):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return None
        result_list = []
        for ids in list_of_ids:
            my_cell = self.get_cell_by_id(ids)
            result_list.append(my_cell)
        return result_list

    def print(self):
        print("Cells: ")
        for cell in self.__cells:
            cell.print()
        self.print_counter()
        self.print_states()
        self.print_feromon()

    def print_states(self):
        print("Current states of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_state_as_string())+"\t"
            print(string)

    def print_feromon(self):
        print("Current feromon of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_feromon())+"\t"
            print(string)

    def print_counter(self):
        print("Current counter of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_counter())+"\t"
            print(string)