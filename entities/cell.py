class Cell:
    __state = None  # Cell can be in 4 states currently: 0 - normal, 1 - start, 2 - finish, 3 - permitted
    __feromone = None

    # todo add counter

    def __init__(self, feromone, state=0):
        # todo add validations of input(waiting only type Int, Double)
        self.__feromone = feromone
        self.__state = state

    def is_normal(self):
        return self.__state == 0

    def is_start(self):
        return self.__state == 1

    # todo add more checkers

    def set_feromon(self, feromone):
        self.__feromone = feromone

    def get_feromon(self):
        return self.__feromone

        # todo add method for calculating and getting value of counter

    def print(self):
        pass