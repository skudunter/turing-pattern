class Cell:
    def __init__(self, pos, vel, acc, color):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.color = color

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
