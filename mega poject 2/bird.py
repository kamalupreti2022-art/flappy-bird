import pygame

class bird(pygame.sprite.Sprite):
    def __init__(self,scale_factor):
        super(bird,self).__init__()
        self.images=[pygame.transform.scale_by(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\birdup.png").convert_alpha(),scale_factor),
        pygame.transform.scale_by(pygame.image.load(r"C:\Users\sunil\Desktop\cc\mega poject 2\New folder\assets\birddown.png").convert_alpha(),scale_factor)]
        self.image_index=0
        self.image=self.images[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed= 250
        self.anim_counter=0
        self.update_on=True

    def update(self, dt):
        if self.update_on==True:
            self.play_animation()
            self.applygravity(dt)
            if self.rect.y <=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

        if self.rect.y>=440 :
            self.rect.y=440 
    def applygravity(self, dt):
        self.y_velocity += self.gravity*dt
        self.rect.y += self.y_velocity

    def flap(self,dt):
        self.y_velocity = -self.flap_speed*dt

    def play_animation(self):
        if self.anim_counter==5:
            self.image=self.images[self.image_index]
            if self.image_index==0:
                self.image_index=1
            else:
                self.image_index=0
            self.anim_counter=0
        self.anim_counter+=1
