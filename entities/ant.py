class Ant:
    __old_cell = None
    __current_cell = None

    def __init__(self):
        pass

    def get_selected_cell_id(self, available_cells):  # available_cells - list of cells
        # todo add logic for finding cell with maximum feromon
        selected_id = 0
        self.move(selected_id)
        return selected_id

    def move(self, new_cell):
        self.__old_cell = self.__current_cell
        self.__current_cell = new_cell