class Cell:
    __state = None  # Cell can be in 4 states currently: 0 - normal, 1 - start, 2 - finish, 3 - permitted
    __feromone = None
    __counter = None

    def __init__(self, feromone, state=0):
        if not isinstance(feromone, float):
            raise TypeError("input feromone is not %s type" % (float))
        if not isinstance(state, int) and (-1 < state < 4):
            raise TypeError("input state is not %s type must be 0,1,2,3" % (int))
        self.__counter = 0
        self.__feromone = feromone
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