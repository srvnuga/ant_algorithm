from entities.cells_group import CellsGroup


class Board:
    __cells = None  # list of cells
    __cells_coords = None  # 2 dimension map to connect Id of cells With X,Y coords

    def __init__(self, size):
        # todo init board with list of cells. length of list must be equal to size
        # id of cell must be different!
        self.cells_coords = CellsGroup()
        self.randomize_cells()
        self.refresh_mapping(self.__cells)

    def refresh_mapping(self, list_cells):
        if isinstance(list_cells, list):
            raise TypeError("list_cells is not a list!")
        self.cells_coords.create_mapping(list_cells)

    def randomize_cells(self):
        list = []
        if self.__cells is None or len(self.__cells) == 0:
            # if list is None or Empty - return without any logic
            return
        else:
            for cell in self.__cells:
                # todo add logic of randomize of cell's feromones
                pass

    def set_start_cell(self):
        # todo add logic to make start cell
        # start cell is the FIRST cell in the list of cell
        # BEFORE need to add method set state in Cell
        pass

    def set_finish_cell(self):
        # todo add logic to make finish cell
        # finish cell is the LAST cell in the list of cell
        # BEFORE need to add method set state in Cell
        pass

    def get_start_cell(self):
        # todo add logic to find and return start cell
        return None

    def get_cell_by_id(self, cell_id):
        # todo  add logic for finding cell by cell_id and return it
        return None

    def get_cells_by_ids(self, list_of_ids):
        # todo add logic for finding list of cells by cells_ids and return it
        # use method get_cell_by_id(cell_id)
        return None

    def print(self):
        # todo add logic for printing this object
        pass
