import pygame

class Ball:
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self, blocks, paddle_rect):
        collision_thresh = 5
        for row in blocks:
            for block in row:
                if self.rect.colliderect(block[0]):
                    # Handle collision with the block here...
                    pass  # Implement collision logic

        # Implement wall and paddle collision here...

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        return 0  # Return game state

    def draw(self, screen):
        pygame.draw.circle(screen, (142, 135, 123), self.rect.center, self.ball_rad)
        pygame.draw.circle(screen, (100, 100, 100), self.rect.center, self.ball_rad, 3)

    def reset(self, x, y):
        self.ball_rad = 10
        self.rect = pygame.Rect(x - self.ball_rad, y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
