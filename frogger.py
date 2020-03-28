import pygame
from froggerlib import frog, stage, road, race_car
import random


class Frogger:
    def __init__(self, screen_width, screen_height, lane_size, rows, cols):
        self.width = screen_width
        self.height = screen_height
        self.mFrog_dead = False
        self.lane_size = lane_size
        self.rows = rows
        self.cols = cols
        self.num_roads = (self.rows - 3)

        x = (self.cols // 2)*self.lane_size
        y = (self.rows - 1)*self.lane_size
        w = self.lane_size
        h = self.lane_size
        self.mFrog = frog.Frog(x, y, w, h, x, y, 10, w, h)

        self.roads = []
        for i in range(self.num_roads):
            x = 0
            y = (self.rows - 2 - i)*self.lane_size
            w = self.width
            h = self.lane_size
            self.roads.append(road.Road(x, y, w, h))
        x = 0
        y1 = (self.rows - 1)*self.lane_size
        y2 = (self.rows + 5)
        w = self.width
        h = self.lane_size
        self.stage1 = stage.Stage(x, y1, w, h)
        self.stage2 = stage.Stage(x, y2, w, h)

        self.racecars = []
        gap = 0.1 * self.lane_size
        for i in range(self.num_roads):
            w = self.lane_size+2*gap
            h = self.lane_size-2*gap
            if i % 2 == 0:
                x = -w
                dx = self.width + w
            else:
                x = self.width
                dx = -w
            y = (self.rows - 2 - i) * self.lane_size + gap
            dy = y
            mins = 5
            maxs = 10
            self.racecars.append(race_car.RaceCar(
                x, y, w, h, dx, dy, mins, maxs))

    def evolve(self, dt):
        for i in range(len(self.racecars)):
            car = self.racecars[i]
            car.move()
            if car.atDesiredLocation():
                if i % 2 == 0:
                    car.setX(-car.getWidth())
                else:
                    car.setX(self.width)
            if car.hits(self.mFrog):
                self.mFrog_dead = True
        if not self.mFrog_dead:
            self.mFrog.move()
        if self.mFrog.outOfBounds(self.width, self.height):
            self.mFrog_dead = True

    def actOnPressUP(self):
        self.mFrog.up()

    def actOnPressDOWN(self):
        self.mFrog.down()

    def actOnPressLEFT(self):
        self.mFrog.left()

    def actOnPressRIGHT(self):
        self.mFrog.right()

    def draw(self, surface):
        # Background
        r = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(surface, (255, 255, 255), r)

        # Stage
        rectangle(surface, self.stage1, (0, 0, 255))
        rectangle(surface, self.stage2, (0, 0, 255))

        # Road
        for road in self.roads:
            rectangle(surface, road, (255, 255, 255))

        # Car
        for car in self.racecars:
            colors = ['255,255,255', '0,0,0']
            rectangle(surface, car, str(random.choice(colors)))

        # Frog
        rectangle(surface, self.mFrog, (94, 221, 95))


def rectangle(surface, obj, color):
    r = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, r)
