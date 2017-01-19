from entities.ant import Ant
from entities.cell import Cell

# testing creating of Ant object
ant1111 = Ant()

# testing creating of Cell object
#cell = Cell()
#cell.set_feromon(123)

a = Cell(1, 9999.0)
b = Cell(2, 888.0)
c = Cell(3, 9999.0)

av_cells = [a, b, c]

selected = ant1111.get_selected_cell_id(av_cells)
print(selected)