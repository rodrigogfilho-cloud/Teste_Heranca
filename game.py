import pygame
from classe_inimigo import Inimigo
from classe_jogador import Jogador
from classe_fantasma import Fantasma
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()


# ==============================================================================
# LOOP PRINCIPAL
# ==============================================================================
def rodar_jogo():
    jogador = Jogador(800 // 2, 600 - 60)
    inimigo = Inimigo(800 // 2, 0)
    fantasma = Fantasma(600 , 0)
    # Alterei os atributos do inimigos

    inimigo.imagem = pygame.image.load("src/img/slime.png")

    # novo inimigo

    inimigo2 = Inimigo(100,0)

    rodando = True
    while rodando:
        relogio.tick(60)
        tela.fill((30, 30, 30))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Atualizações chamadas individualmente com métodos de nomes diferentes
        jogador.mover(teclas)
        inimigo.mover()
        inimigo2.mover()
        fantasma.mover()

        # Desenho chamado individualmente
        jogador.desenhar(tela)
        inimigo.desenhar(tela)
        inimigo2.desenhar(tela)
        fantasma.desenhar(tela)

        pygame.display.update()

if __name__ == "__main__":
    rodar_jogo()