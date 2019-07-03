import pygame

pygame.init()
screen = pygame.display.set_mode(size=(200, 200))

pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

shouldQuit = False

while not shouldQuit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            shouldQuit = True
            break
    pygame.display.flip()

# Comment is on drawrect e bawww
