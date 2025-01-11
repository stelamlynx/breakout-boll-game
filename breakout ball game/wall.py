import pygame

class Wall:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width // 6
        self.height = 50
        self.create_wall()

    def create_wall(self):
        self.blocks = []
        for row in range(6):
            block_row = []
            for col in range(6):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                strength = 3 if row < 2 else 2 if row < 4 else 1
                block_row.append([rect, strength])
            self.blocks.append(block_row)

    def draw(self):
        for row in self.blocks:
            for block in row:
                rect, strength = block
                color = (69, 177, 232) if strength == 3 else (86, 174, 87) if strength == 2 else (242, 85, 96)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (234, 218, 184), rect, 2)
