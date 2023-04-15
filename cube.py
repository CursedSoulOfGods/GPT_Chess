import pygame
from pygame.locals import *

pygame.init()

# Set the size of the window
size = (800, 800)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("8x8 Cartesian Plane")

# Define the size of each point and the spacing between them
point_size = 25
point_spacing = point_size * 1

# Define the position of the plane
plane_position = [size[0]/2, size[1]/2]

# Define the colors of the points
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

circle_positions = []

# Draw the points on the screen
for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            rect_color = RED
        else:
            rect_color = WHITE
        rect = pygame.Rect(int(plane_position[0] + (x - 3.5) * point_spacing), int(plane_position[1] + (y - 3.5) * point_spacing), point_size, point_size)
        pygame.draw.rect(screen, rect_color, rect)
        if y == 1 or y == 6:
            circle_rect = pygame.Rect(int(plane_position[0] + (x - 3.5) * point_spacing - point_size/50), int(plane_position[1] + (y - 3.5) * point_spacing - point_size/50), point_size, point_size)
            circle_center = circle_rect.center
            pygame.draw.circle(screen, BLUE, circle_rect.center, int(point_size/3))
            circle_positions.append(circle_center)

# Update the screen
pygame.display.flip()

# Run the game loop
running = True
selected_circle = None
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print("Got Mouse Position")
            # Check if the mouse clicked on a circle
            for i, circle_pos in enumerate(circle_positions):
                print("Moving Circle")
                if pygame.Rect(circle_pos[0] - point_size/2, circle_pos[1] - point_size/2, point_size, point_size).collidepoint(mouse_pos):
                    selected_circle = i
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_circle = None
        elif event.type == pygame.MOUSEMOTION:
            # Check if a circle is currently being dragged
            if selected_circle is not None:
                circle_pos = circle_positions[selected_circle]
                # Move the circle to the new mouse position
                circle_positions[selected_circle] = (circle_pos[0] + event.rel[0], circle_pos[1] + event.rel[1])
                # Redraw the screen
                screen.fill(WHITE)
                for x in range(8):
                    for y in range(8):
                        if (x + y) % 2 == 0:
                            rect_color = RED
                        else:
                            rect_color = WHITE
                        rect = pygame.Rect(int(plane_position[0] + (x - 3.5) * point_spacing), int(plane_position[1] + (y - 3.5) * point_spacing), point_size, point_size)
                        pygame.draw.rect(screen, rect_color, rect)
                        if y == 1 or y == 6:
                            circle_rect = pygame.Rect(int(plane_position[0] + (x - 3.5) * point_spacing - point_size/50), int(plane_position[1] + (y - 3.5) * point_spacing - point_size/50), point_size, point_size)
                            circle_center = circle_rect.center
                            pygame.draw.circle(screen, BLUE, circle_rect.center, int(point_size/3))
                            circle_positions.append(circle_center)
# Quit the game
pygame.quit()