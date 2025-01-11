import pygame

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.reset(screen_width, screen_height)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (142, 135, 123), self.rect)
        pygame.draw.rect(screen, (100, 100, 100), self.rect, 3)

    def reset(self, screen_width, screen_height):
        self.width = screen_width // 6
        self.height = 20
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - self.height * 2
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
