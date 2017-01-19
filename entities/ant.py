import random

class Ant:
    __old_cell = None
    __current_cell = None

    def __init__(self):
        pass

    def get_selected_cell_id(self, available_cells):  # available_cells - list of cells
        if not isinstance(available_cells, list):
            raise TypeError("input available_cells is not %s type" % (list))
        max_feromon = 0.0
        for cell in available_cells:
            if cell.get_feromon() > max_feromon:
                max_feromon = cell.get_feromon()
        max_cells = []
        for cell in available_cells:
            if cell.get_feromon() is max_feromon:
                max_cells.append(cell)
        selected_id = None
        if len(max_cells) == 1:
            selected_id = max_cells[0].get_id()
        else:
            random_cell = random.randrange(0, len(max_cells), 1)
            selected_id = max_cells[random_cell].get_id()
        self.move(selected_id)
        return selected_id

    def move(self, new_cell):
        self.__old_cell = self.__current_cell
        self.__current_cell = new_cell