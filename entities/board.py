class Board:
    __cells = None  # 2 dimension list of cells

    def __init__(self, size):
        # todo init board with list of cells. length of list must be equal to size
        # id of cell must be different!
        self.randomize_cells()

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
        pass

    def set_finish_cell(self):
        pass

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