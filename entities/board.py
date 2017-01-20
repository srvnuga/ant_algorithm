from entities.cell import Cell
from entities.cells_group import CellsGroup
import random
import math


class Board:
    __cells = None  # list of cells
    __cells_coords = None  # 2 dimension map to connect Id of cells With X,Y coords

    def __init__(self, size):
        self.__cells_coords = CellsGroup()
        self.__create_board(size)
        self.randomize_cells()
        self.__refresh_mapping(self.__cells)
        self.set_finish_cell()
        self.set_start_cell()
        self.__create_permitted_cell()

    def __create_board(self, size):
        self.__cells = []
        if size <= 0:
            raise TypeError("Size can't be < 0")
        for cellid in range(0, size):
            c = Cell(cellid)
            self.__cells.append(c)

    def __refresh_mapping(self, list_cells):
        if not isinstance(list_cells, list):
            raise TypeError("list_cells is not a list!")
        self.__cells_coords.create_mapping(list_cells)

    def randomize_cells(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            for cell in self.__cells:
                c = random.randrange(0, 10, 1)
                b = random.randrange(0, 10, 1)
                feromon = c + b * 0.1
                cell.set_feromon(feromon)

    def __create_permitted_cell(self):
        random_id = random.randrange(1, len(self.__cells) - 2, 1)
        self.__cells[random_id].set_cell_state(3)
        random_id = random.randrange(1, len(self.__cells) - 2, 1)
        self.__cells[random_id].set_cell_state(3)
        random_id = random.randrange(1, len(self.__cells) - 2, 1)
        #self.__cells[random_id].set_cell_state(3)
        random_id = random.randrange(1, len(self.__cells) - 2, 1)
        #self.__cells[random_id].set_cell_state(3)

    def set_start_cell(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            self.__cells[0].set_cell_state(1)

    def set_finish_cell(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        else:
            self.__cells[len(self.__cells) - 1].set_cell_state(2)

    def get_start_cell_id(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        for cell in self.__cells:
            if cell.is_start():
                return cell.get_id()

    def get_finish_cell_id(self):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return
        for cell in self.__cells:
            if cell.is_finish():
                return cell.get_id()

    def __get_cell_by_id(self, cell_id):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return None
        else:
            for cell in self.__cells:
                if cell.get_id() == cell_id:
                    return cell
            raise TypeError("Can not find cell with id = %d" % cell_id)

    def __get_cells_by_ids(self, list_of_ids):
        if self.__cells is None or len(self.__cells) == 0:  # if list is None or Empty - return without any logic
            return None
        result_list = []
        for ids in list_of_ids:
            my_cell = self.__get_cell_by_id(ids)
            result_list.append(my_cell)
        return result_list

    def get_available_cells_by_id(self, current_id, old_id):
        available_ids = self.__cells_coords.get_available_ids_by_id(current_id, old_id)
        if len(available_ids) == 0:
            raise TypeError("No available ids, Sorry try again")
        available_cells = self.__get_cells_by_ids(available_ids)
        no_permitted_cells = self.__get_no_permitted_cells(available_cells)
        if len(no_permitted_cells) == 0:
            raise TypeError("Sorry, there're no available cells for ant")
        return no_permitted_cells

    def __get_no_permitted_cells(self, list_of_cells):
        result_cells = []
        for cell in list_of_cells:
            if not cell.is_permitted():
                result_cells.append(cell)
        return result_cells

    def print(self):
        print("Cells: ")
        self.print_counter()
        self.print_states()
        self.print_feromon()

    def print_states(self):
        print("Current states of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_state_as_string()) + "\t"
            print(string)

    def print_feromon(self):
        print("Current feromon of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_feromon()) + "\t"
            print(string)

    def print_counter(self):
        print("Current counter of cells:")
        l = int(math.sqrt(len(self.__cells)))
        for i in range(0, l):
            string = ""
            for j in range(0, l):
                string += str(self.__cells[i * l + j].get_counter()) + "\t"
            print(string)