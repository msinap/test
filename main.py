import pygame

pygame.init()
screen = pygame.display.set_mode(size=(100, 100))

done = False

while not done:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            done = True
            break
    pygame.display.flip()
