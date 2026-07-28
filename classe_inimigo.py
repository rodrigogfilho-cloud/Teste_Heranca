import pygame

class Inimigo:
    def __init__(self, x, y):
        # Repetição de dados estruturais básicos
        self.imagem = pygame.image.load("src/img/bomba.png")
        self.imagem = pygame.transform.scale(self.imagem,(30,50))
        self.velocidade_y = 3
        self.pos_x = x
        self.pos_y = y
        

    def mover_inimigo(self):
        self.pos_y += self.velocidade_y
        if self.pos_y > 600:
            self.pos_y = -100

    def desenhar(self, superficie):
        superficie.blit(self.imagem,(self.pos_x, self.pos_y))