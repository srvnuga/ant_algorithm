class Mapping:
    __id = None
    __x = None
    __y = None

    def __init__(self, cell_id, x, y):
        if not isinstance(cell_id, int) or not isinstance(x, int) or not isinstance(y, int):
            pass
            #raise TypeError("input id, x, y must be Int")
        self.__id = cell_id
        self.__x = x
        self.__y = y

    def get_id(self):
        return self.__id

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y