import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 400))
print('Setup Start')

print('Loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()  # close Window
            quit()  # end pygame
