import pygame
from random import randint

class pipe:
    def __init__(self, scale_factor,move_speed):
        self.pipeup=pygame.transform.scale_by(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\pipeup.png").convert_alpha(),scale_factor)
        self.pipedown=pygame.transform.scale_by(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\pipedown.png").convert_alpha(),scale_factor)
        self.rect_up=self.pipeup.get_rect()
        self.rect_down=self.pipedown.get_rect()
        self.pipe_dist=130
        self.rect_up.y=randint(150,400)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipe_dist-self.rect_down.height
        self.rect_down.x=600
        self.move_speed=move_speed
        self.pipes=[self.rect_up,self.rect_down]

    def draw(self, screen):
        screen.blit(self.pipeup, self.rect_up)
        screen.blit(self.pipedown, self.rect_down)

    def update(self, dt):
        self.rect_up.x -= self.move_speed * dt
        self.rect_down.x -= self.move_speed * dt    

