class Ant:
    __old_cell = None
    __current_cell = None

    def __init__(self):
        pass

    def get_selected_cell_id(self, available_cells):  # available_cells = это список
        selected_id = 0
        self.__old_cell = self.__current_cell
        self.__current_cell = selected_id
        return selected_id


