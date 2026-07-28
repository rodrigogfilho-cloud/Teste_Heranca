import pygame

class Jogador:
    def __init__(self, x, y):
        # Repetição de dados estruturais básicos
        self.imagem = pygame.image.load("src/img/aviao.png")
        self.velocidade = 5
        self.pos_x = x
        self.pos_y = y

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.pos_x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.pos_x += self.velocidade
        if teclas[pygame.K_UP]:
            self.pos_y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.pos_y += self.velocidade

    def desenhar(self, superficie):
        superficie.blit(self.imagem,(self.pos_x,self.pos_y))
