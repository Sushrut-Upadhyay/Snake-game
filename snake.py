import pygame
from pygame.locals import *
import time
import random

size=84
class Apple:
    def __init__(self,parent_screen):
        self.img=pygame.image.load('Snake game/resources/apple.png')
        self.parent_screen=parent_screen
        self.a=168
        self.b=168

    def draw(self):
        self.parent_screen.blit(self.img,(self.a,self.b))
        pygame.display.flip()

    def move(self):
        self.a=random.randint(0,13)*size
        self.b=random.randint(0,5)*size



class Snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=pygame.image.load('Snake game/resources/snakeball.png')
        self.x=[size]*length
        self.y=[size]*length
        self.direction='down'

    def draw(self):
        self.parent_screen.fill((28, 29, 79))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction='left'

    def move_right(self):
        self.direction='right'

    def move_up(self):
        self.direction='up'

    def move_down(self):
        self.direction='down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            self.y[0]-=size
        if self.direction=='down':
            self.y[0]+=size
        if self.direction=='left':
            self.x[0]-=size
        if self.direction=='right':
            self.x[0]+=size

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1176,504))
        surface=pygame.display.set_caption("SNAKE")
        self.surface.fill((28, 29, 79))
        self.snake=Snake(self.surface,5)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()
    
    def is_collision(self,x1,y1,x2,y2):
        if x1==x2 and y1==y2: #or x1==x2+size
            return True
        #if y1+size==y2 or y1==y2+size:    
               # return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.a,self.apple.b):
            self.apple.move()

    
    
    def run(self):
        running=True
        while running:
            for i in pygame.event.get():
                if i.type==KEYDOWN:
                    if i.key==K_ESCAPE:
                        running=False
                    if i.key==K_UP:
                        self.snake.move_up()
                    if i.key==K_DOWN:
                        self.snake.move_down()
                    if i.key==K_LEFT:
                        self.snake.move_left()
                    if i.key==K_RIGHT:
                        self.snake.move_right()
    
                elif i.type==QUIT:
                    running=False
            self.play()
            time.sleep(0.2)
   

if __name__=="__main__":
    game=Game()
    game.run() 