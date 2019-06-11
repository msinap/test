import pygame

pygame.init()
screen = pygame.display.set_mode(size=(500, 500))

pygame.draw.circle(screen, (255, 255, 255), (200, 200), 100, 1)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    pygame.display.flip()
