import pygame
class Paddle:
    Color = (255,255,255)
    Vel = 4
    def __init__(self,x,y,w,h,):
        self.ogx = x
        self.ogy = y
        self.x = x 
        self.y = y
        self.height = h
        self.width = w
    def draw(self,win):
        pygame.draw.rect(win,self.Color,(self.x,self.y,self.width,self.height))
    def move(self,up=True):
        if up:
            self.y -= self.Vel
        else:
            self.y += self.Vel
    def reset(self):
        self.x = self.ogx
        self.y = self.ogy
class Ball:
    Color = (255,255,255)
    maxv = 5
    def __init__(self,x,y,r):
        self.ogx = x
        self.ogy = y
        self.x = x
        self.y = y        
        self.rad = r
        self.x_vel = self.maxv
        self.y_vel = 0
    
    def draw(self,win):
        pygame.draw.circle(win,self.Color,(self.x,self.y),self.rad)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def reset(self):
        self.x = self.ogx
        self.y = self.ogy
        self.y_vel = 0
        self.x_vel *= -1