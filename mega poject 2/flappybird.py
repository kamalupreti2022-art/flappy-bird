import pygame
import sys
import time
from bird import bird
from pipe import pipe

pygame.init()
class game:
    def __init__(self):
        self.move_speed=100
        self.clock=pygame.time.Clock()
        self.height=600
        self.width=400
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.bird=bird(scale_factor=1.0)
        self.pipes=[]
        self.pipe_generate_counter=1
        self.isenterpressed=False
        self.startmonitoring=False
        self.score=0
        self.font=pygame.font.Font(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\font.ttf",15)
        self.score_text=self.font.render("score:0",True,(255,255,255))
        self.score_text_rect=self.score_text.get_rect(center=(50,20))
        self.restart_text=self.font.render("RESTART",True,(255,0,0))
        self.restart_text_rect=self.restart_text.get_rect(center=(200,300))
        self.setUpBgAndGround()
        self.is_game_started=True
        self.check_score()
        self.gameloop()

        
    def gameloop(self):
        last_time=time.time()
        while True:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN and self.is_game_started:
                        self.isenterpressed=True
                        # self.update_on=True 
                    if event.key==pygame.K_SPACE and self.isenterpressed:
                        self.bird.flap(dt)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.restart_text_rect.collidepoint(event.pos) and not self.is_game_started:
                        self.restartGame()

            self.update_everything(dt)
            self.check_collision()
            self.check_score()
            self.draw_everything()
            pygame.display.update()
            self.clock.tick(60)
            

    def setUpBgAndGround(self):
        self.bg_img=pygame.transform.scale(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\bg.png").convert(),(400,500))
        self.ground1_img=pygame.transform.scale(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\ground.png").convert(),(400,467))
        self.ground2_img=pygame.transform.scale(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\ground.png").convert(),(400,467))
        

        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()

        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=467
        self.ground2_rect.y=467
        self.bird_rect=self.bird.image.get_rect()

    def draw_everything(self):
        self.screen.blit(self.bg_img,(0,0))
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.screen.blit(self.ground1_img,self.ground1_rect)
        self.screen.blit(self.ground2_img,self.ground2_rect)
        self.screen.blit(self.bird.image,self.bird.rect )
        self.screen.blit(self.score_text,self.score_text_rect)
        if not self.is_game_started:
            self.screen.blit(self.restart_text,self.restart_text_rect)


    def update_everything(self,dt):
        if self.isenterpressed==True:
            
            self.ground1_rect.x -= self.move_speed * dt
            self.ground2_rect.x -= self.move_speed * dt

            if self.ground1_rect.right <= 0:
                self.ground1_rect.x = self.ground2_rect.right

            if self.ground2_rect.right <= 0:
                self.ground2_rect.x = self.ground1_rect.right

            if self.pipe_generate_counter>100:
                self.pipes.append(pipe(scale_factor=1.0,move_speed=self.move_speed))
                self.pipe_generate_counter=0
                print("pipe generated")
            self.pipe_generate_counter+=1
            for p in self.pipes:
                p.update(dt)

            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)
                    print("pipe removed")
                    
        if self.isenterpressed or not self.is_game_started:
            self.bird.update(dt)

    def check_collision(self):
        if self.bird.rect.bottom >= 460:
            self.isenterpressed = False
            self.bird.update_on = False
            self.is_game_started=False
        for pipes in self.pipes:
            if self.bird.rect.colliderect(self.pipes[0].rect_up) or self.bird.rect.colliderect(self.pipes[0].rect_down):
                self.isenterpressed = False
                self.is_game_started=False

    def check_score(self):
        if len(self.pipes)>0:
            if self.bird.rect.left>self.pipes[0].rect_down.left and self.bird.rect.right>self.pipes[0].rect_down.right and not self.startmonitoring:
                self.startmonitoring=True
            if self.bird.rect.right<self.pipes[0].rect_down.right and self.startmonitoring:
                self.startmonitoring=False
                self.score +=1
                self.score_text=self.font.render(f"score:{self.score}",True,(255,255,255))

    def restartGame(self):
        self.bird=bird(scale_factor=1.0)
        self.pipes=[]
        self.pipe_generate_counter=1
        self.isenterpressed=False
        self.startmonitoring=False
        self.score=0
        self.score_text=self.font.render("score:0",True,(255,255,255))
        self.is_game_started=True

game()
