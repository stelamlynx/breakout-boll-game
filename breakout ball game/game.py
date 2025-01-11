import paddle
from paddle import Paddle
from ball import Ball
from wall import Wall
from utils import draw_text

class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Breakout')
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.bg_color = (234, 218, 184)

        self.wall = Wall(self.screen_width, self.screen_height)
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.paddle.rect.centerx, self.paddle.rect.top)
        
        self.live_ball = False
        self.game_over = 0

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.screen.fill(self.bg_color)
            self.handle_events()
            self.update_game()
            self.draw_elements()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not self.live_ball:
                self.start_game()

    def start_game(self):
        self.live_ball = True
        self.ball.reset(self.paddle.rect.centerx, self.paddle.rect.top)
        self.paddle.reset()
        self.wall.create_wall()

    def update_game(self):
        if self.live_ball:
            self.paddle.move()
            self.game_over = self.ball.move(self.wall.blocks, self.paddle.rect)
            if self.game_over != 0:
                self.live_ball = False

    def draw_elements(self):
        self.wall.draw()
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)

        if not self.live_ball:
            if self.game_over == 0:
                draw_text(self.screen, 'BREAKOUT GAME USING PYTHON', 15, self.screen_height // 2 + 50)
                draw_text(self.screen, 'CLICK TO START GAME', 100, self.screen_height // 2 + 100)
            elif self.game_over == 1:
                draw_text(self.screen, 'YOU WON!', 240, self.screen_height // 2 + 50)
                draw_text(self.screen, 'CLICK TO RESTART', 100, self.screen_height // 2 + 100)
            elif self.game_over == -1:
                draw_text(self.screen, 'YOU LOST!', 240, self.screen_height // 2 + 50)
                draw_text(self.screen, 'CLICK TO RESTART', 100, self.screen_height // 2 + 100)
