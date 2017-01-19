from entities.ant import Ant
from entities.board import Board
from entities.cell import Cell

# testing creating of Ant object
ant1111 = Ant()

# testing creating of Cell object
#cell = Cell()
#cell.set_feromon(123)

a = Cell(1, feromone=9999.0)
b = Cell(2,  feromone=888.0)
c = Cell(3,  feromone=9999.0)

'''av_cells = [a, b, c]

selected = ant1111.get_selected_cell_id(av_cells)
print(selected)'''

b = Board(4)
b.get_cell_by_id(2)







