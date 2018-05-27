# Ben-Ryder 2018

import pygame
from pygame_gui.image import *

class checkbox:
    def __init__(self,rest_image,hover_image,active_image,active_hover_image):
        self.rest_image = image(rest_image)
        self.hover_image = image(hover_image)
        self.active_image = image(active_image)
        self.active_hover_image = image(active_hover_image)
        self.rect = self.rest_image.image.get_rect()
        self.active = False

    def mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def check_clicked(self):
        if self.mouse_over():
            self.active = not self.active
            return True
        return False
    
    def draw(self,display,x,y):
        self.rect[0],self.rect[1] = x,y
        if self.mouse_over():
            if self.active:
                self.active_hover_image.draw(display,x,y)
            else:
                self.hover_image.draw(display,x,y)
        else:
            if self.active:
                self.active_image.draw(display,x,y)
            else:
                self.rest_image.draw(display,x,y)