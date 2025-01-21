import pygame
from constants import WIDTH, HEIGHT, BEIGE,FPS
#from board.board import create_board

pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f"Прахосница {FPS}fps")

def main():


    clock = pygame.time.Clock()
   # board = create_board()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(BEIGE)  # White background
        # Rendering logic here
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
if __name__ == "__main__":
    main()