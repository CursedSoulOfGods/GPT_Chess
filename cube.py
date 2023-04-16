import pygame
from pygame.locals import *

pygame.init()

# Set the size of the window
size = (800, 800)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("8x8x8 Cube Simulation")

# Define the size of the cube
cube_size = 100

# Define the position of the cube
cube_position = (size[0]/2, size[1]/2)

# Define the colors of the cube faces
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Function to draw the cube
def draw_cube(position):
    x, y = position

    # Draw the front face of the cube
    pygame.draw.rect(screen, RED, (x-cube_size/2, y-cube_size/2, cube_size, cube_size))

    # Draw the back face of the cube
    pygame.draw.polygon(screen, GREEN, [(x-cube_size/2, y-cube_size/2), (x+cube_size/2, y-cube_size/2), (x+cube_size/2, y+cube_size/2), (x-cube_size/2, y+cube_size/2)])

    # Draw the top face of the cube
    pygame.draw.polygon(screen, BLUE, [(x-cube_size/2, y-cube_size/2), (x-cube_size/2+10, y-cube_size/2-10), (x+cube_size/2+10, y-cube_size/2-10), (x+cube_size/2, y-cube_size/2)])

    # Draw the bottom face of the cube
    pygame.draw.polygon(screen, YELLOW, [(x-cube_size/2, y+cube_size/2), (x-cube_size/2+10, y+cube_size/2-10), (x+cube_size/2+10, y+cube_size/2-10), (x+cube_size/2, y+cube_size/2)])

    # Draw the left face of the cube
    pygame.draw.polygon(screen, ORANGE, [(x-cube_size/2, y-cube_size/2), (x-cube_size/2+10, y-cube_size/2-10), (x-cube_size/2+10, y+cube_size/2-10), (x-cube_size/2, y+cube_size/2)])

    # Draw the right face of the cube
    pygame.draw.polygon(screen, PURPLE, [(x+cube_size/2, y-cube_size/2), (x+cube_size/2+10, y-cube_size/2-10), (x+cube_size/2+10, y+cube_size/2-10), (x+cube_size/2, y+cube_size/2)])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the cube
    draw_cube(cube_position)

    # Update the screen
    pygame.display.update()

pygame.quit()