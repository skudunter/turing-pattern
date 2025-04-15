import pygame
from cell import Cell


class Simulation:
    def __init__(self, screen, num_cells, width):
        self.num_cells = num_cells
        self.cell_width = round(width / num_cells)
        self.screen = screen
        self.grid = [[0 for i in range(num_cells)] for j in range(num_cells)]
        self.display_cells = True

    def update(self):
        self.update_cells_in_grid()
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return
                cell.update()

    def display(self):
        for i in range(self.num_cells):
            for j in range(self.num_cells):
                pygame.draw.rect(self.screen, (23, 25, 26), (i * self.cell_width,
                                                             j * self.cell_width, self.cell_width, self.cell_width), 1)
        # display cells in grid
        if self.display_cells:
            for row in self.grid:
                for cell in row:
                    if cell == 0:
                        return
                    pygame.draw.ellipse(
                        self.screen, cell.color, (cell.pos, (3, 3)))

    def update_cells_in_grid(self):
        # update the index for each cell in the grid
        grid = [0 for i in range(self.num_cells)
                for j in range(self.num_cells)]

        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return
                dx = round(cell.pos[0]/self.cell_width)
                dy = round(cell.pos[1]/self.cell_width)
                grid[dx][dy].append(cell)
