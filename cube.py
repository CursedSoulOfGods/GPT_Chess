import pygame
from pygame.locals import *

pygame.init()

# Set the size of the window
size = (800, 800)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("8x8 Cartesian Plane")

# Define the size of each point and the spacing between them
point_size = 10
point_spacing = point_size * 2

# Define the position of the plane
plane_position = [size[0]/2, size[1]/2]

# Define the color of the points
WHITE = (255, 255, 255)

# Draw the points on the screen
for x in range(8):
    for y in range(8):
        rect = pygame.Rect(int(plane_position[0] + (x - 3.5) * point_spacing), int(plane_position[1] + (y - 3.5) * point_spacing), point_size, point_size)
        pygame.draw.rect(screen, WHITE, rect)
# Update the screen
pygame.display.flip()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
