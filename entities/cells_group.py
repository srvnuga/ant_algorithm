import math

from entities.mapping.mapping import Mapping


class CellsGroup:
    __cell_coords = None

    def __init__(self):
        self.__cell_coords = []

    def get_x_by_id(self, id):
        for mapp in self.__cell_coords:
            if mapp.get_id() == id:
                return mapp.get_x()

    def get_y_by_id(self, id):
        for mapp in self.__cell_coords:
            if mapp.get_id() == id:
                return mapp.get_y()

    def get_id_by_xy(self, x, y):
        for mapp in self.__cell_coords:
            if mapp.get_x() == x and mapp.get_y() == y:
                return mapp.get_id()

    def create_mapping(self, list_ids):
        if not isinstance(list_ids, list):
            raise TypeError("list_ids is not a list")
        # get sqrt(length)
        sq_len = math.sqrt(len(list_ids))
        if sq_len - int(sq_len) is not 0:
            raise AttributeError("list_ids has a length which is not a full square")
        # empty cell-coords-mapping
        self.__cell_coords = []

        for x in range(0, sq_len):
            for y in range(0, sq_len):
                mapping = Mapping(list_ids[sq_len * x + y], x, y)
                self.__cell_coords.add(mapping)

    def get_available_ids_by_id(self, current_id):
        current_x = self.get_x_by_id(current_id)
        current_y = self.get_y_by_id(current_id)
        result_ids = []
        up_cell_id = self.get_id_by_xy(current_x - 1, current_y)
        if up_cell_id is not None:
            result_ids.append(up_cell_id)
        down_cell_id = self.get_id_by_xy(current_x + 1, current_y)
        if down_cell_id is not None:
            result_ids.append(down_cell_id)
        right_cell_id = self.get_id_by_xy(current_x, current_y + 1)
        if right_cell_id is not None:
            result_ids.append(right_cell_id)
        left_cell_id = self.get_id_by_xy(current_x, current_y - 1)
        if left_cell_id is not None:
            left_cell_id.append(down_cell_id)
        return result_ids