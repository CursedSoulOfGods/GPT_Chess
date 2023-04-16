import pygame
from pygame.locals import *
import math

pygame.init()

# Set the size of the window
size = (800, 800)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("8x8x8 Cube Simulation")

# Define the size of the cube
cube_size = 100

# Define the position of the cube
cube_position = [size[0]/2, size[1]/2]

# Define the colors of the cube faces
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Define the vertices of the cube
vertices = [    [-cube_size/2, -cube_size/2, -cube_size/2],
    [cube_size/2, -cube_size/2, -cube_size/2],
    [cube_size/2, cube_size/2, -cube_size/2],
    [-cube_size/2, cube_size/2, -cube_size/2],
    [-cube_size/2, -cube_size/2, cube_size/2],
    [cube_size/2, -cube_size/2, cube_size/2],
    [cube_size/2, cube_size/2, cube_size/2],
    [-cube_size/2, cube_size/2, cube_size/2],
]

# Define the edges of the cube
edges = [    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]

# Function to rotate the cube
def rotate_cube(theta, axis):
    rotation_matrix = []
    if axis == "x":
        rotation_matrix = [            [1, 0, 0],
            [0, math.cos(theta), -math.sin(theta)],
            [0, math.sin(theta), math.cos(theta)]
        ]
    elif axis == "y":
        rotation_matrix = [            [math.cos(theta), 0, math.sin(theta)],
            [0, 1, 0],
            [-math.sin(theta), 0, math.cos(theta)]
        ]
    elif axis == "z":
        rotation_matrix = [            [math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta), math.cos(theta), 0],
            [0, 0, 1]
        ]
    for i in range(len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]
        z = vertices[i][2]
        vertices[i][0] = x*rotation_matrix[0][0] + y*rotation_matrix[0][1] + z*rotation_matrix[0][2]
        vertices[i][1] = x*rotation_matrix[1][0] + y*rotation_matrix[1][1] + z*rotation_matrix[1][2]
        vertices[i][2] = x*rotation_matrix[2][0] + y*rotation_matrix[2][1] + z*rotation_matrix[2][2]

# Function to draw the cube
def draw_cube(position):