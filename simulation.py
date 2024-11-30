import pygame
from cell import Cell


class Simulation:
    def __init__(self, screen, num_cells, width):
        self.num_cells = num_cells
        self.cell_width = round(width / num_cells)
        self.screen = screen
        self.cells = [Cell((100,100),(1,1),(23,255,0))]
        self.display_cells = True

    def display(self):
        for i in range(self.num_cells):
            for j in range(self.num_cells):
                pygame.draw.rect(self.screen, (255, 255, 255), (i * self.cell_width,
                                                                j * self.cell_width, self.cell_width, self.cell_width), 0)
        # display cells
        if self.display_cells:
            for cell in self.cells:
                pygame.draw.ellipse(self.screen, cell.color, (cell.pos, (3, 3)))
