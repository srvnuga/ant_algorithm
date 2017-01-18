import math

from entities.mapping.mapping import Mapping


class CellsGroup:
    __N = None
    __cell_coords = None

    def __init__(self):
        pass

    def create_mapping(self, list_ids):
        if not isinstance(list_ids, list):
            raise TypeError("list_ids is not a list")
        sq_len = math.sqrt(len(list_ids))
        if sq_len - int(sq_len) is not 0:
            raise AttributeError("list_ids has a length which is not a full square")
        # empty cell-coords-mapping
        self.__cell_coords = []

        for x in range(0, sq_len):
            for y in range(0, sq_len):
                mapping = Mapping(list_ids[sq_len * x + y], x, y)
                self.__cell_coords.add(mapping)