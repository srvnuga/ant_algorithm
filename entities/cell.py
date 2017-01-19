class Cell:
    __state = None  # Cell can be in 4 states currently: 0 - normal, 1 - start, 2 - finish, 3 - permitted
    __feromone = None
    __counter = None
    __cell_id = None

    def __init__(self, cell_id, feromone=0.0, state=0):
        if not isinstance(feromone, float):
            raise TypeError("input feromone is not %s type" % (float))
        self.__cell_id = cell_id
        self.__counter = 0
        self.__feromone = feromone
        self.set_cell_state(state)

    def get_id(self):
        return self.__cell_id


    def set_cell_state(self, state):
        if not isinstance(state, int) and (-1 < state < 4):
            raise TypeError("input state is not %s type must be 0,1,2,3" % (int))
        self.__state = state


    def is_normal(self):
        return self.__state == 0

    def is_start(self):
        return self.__state == 1

    def is_finish(self):
        return self.__state == 2

    def is_permitted(self):
        return self.__state == 3

    def set_feromon(self, feromone):
        self.__feromone = feromone

    def get_feromon(self):
        return self.__feromone

    def increase_counter(self):
        self.__counter += 1

    def get_counter(self):
        return self.__counter

    def print(self):
        print(self.__counter, self.__feromone, self.__state)
