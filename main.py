import pygame
import game
import frogger

TITLE = "Frogger"
LANE_SIZE = 50
ROWS = 11
COLUMNS = 19
WINDOW_WIDTH = COLUMNS*LANE_SIZE
WINDOW_HEIGHT = ROWS*LANE_SIZE
DESIRED_RATE = 30


class PygameApp(game.Game):

    def __init__(self, title, width, height, frame_rate):
        super().__init__(title, width, height, frame_rate)
        self.mGame = frogger.Frogger(width, height, LANE_SIZE, ROWS, COLUMNS)

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        if pygame.K_UP in newkeys:
            self.mGame.actOnPressUP()
        elif pygame.K_DOWN in newkeys:
            self.mGame.actOnPressDOWN()
        elif pygame.K_LEFT in newkeys:
            self.mGame.actOnPressLEFT()
        elif pygame.K_RIGHT in newkeys:
            self.mGame.actOnPressRIGHT()

        self.mGame.evolve(dt)

    def paint(self, surface):
        self.mGame.draw(surface)


def main():
    pygame.font.init()
    game = PygameApp(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE)
    game.main_loop()


if __name__ == "__main__":
    main()
