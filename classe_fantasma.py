import pygame
from classe_inimigo import Inimigo

class Fantasma (Inimigo):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.imagem = pygame.image.load("src/img/fantasma.png")
        self.contador_tempo = 0
    def desenhar(self, superficie):
        self.contador_tempo += 1 
        if self.contador_tempo == 30:
            self.imagem.set_alpha(self.imagem.get_alpha() + 30)
            self.contador_tempo == 0
        superficie.blit(self.imagem,(self.pos_x,self.pos_y))
