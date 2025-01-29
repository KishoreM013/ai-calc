import pygame
import sys

pygame.init()

height, width = 600, 1000

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI-Powered-Calc")
surface = pygame.Surface((width, height))
surface.fill(white)

running = True 
drawing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True 
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False 
            last_pos = -1
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(surface, black, current_pos, last_pos, 2)
            last_pos = current_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                surface.fill(white)
            elif event.key == pygame.K_RETURN:
                pygame.image.save(surface, "image.jpg")
    screen.blit(surface, (0, 0))
    pygame.display.update()
            

pygame.quit()
sys.exit()