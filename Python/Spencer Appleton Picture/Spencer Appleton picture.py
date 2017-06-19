"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = 3.14
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Spencer pygame 2")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.line(screen, GREEN, [0, 0], [1000, 100], 10)
    pygame.draw.line(screen, RED, [0, 10], [1000, 110], 10) 
    pygame.draw.line(screen, GREEN, [0, 20], [1000, 120], 10) 
    pygame.draw.line(screen, RED, [0, 30], [1000, 130], 10) 
    pygame.draw.line(screen, GREEN, [0, 40], [1000, 140], 10) 
    pygame.draw.line(screen, RED, [0, 50], [1000, 150], 10) 
    pygame.draw.line(screen, GREEN, [0, 60], [1000, 160], 10) 
    pygame.draw.line(screen, RED, [0, 70], [1000, 170], 10) 
    pygame.draw.line(screen, GREEN, [0, 80], [1000, 180], 10) 
    pygame.draw.line(screen, RED, [0, 90], [1000, 190], 10) 
    pygame.draw.line(screen, GREEN, [0, 100], [1000, 190], 10)    
    pygame.draw.line(screen, RED, [0, 110], [1000, 200], 10) 
    pygame.draw.line(screen, GREEN, [0, 120], [1000, 210], 10)    
    pygame.draw.line(screen, RED, [0, 130], [1000, 220], 10) 
    pygame.draw.line(screen, GREEN, [0, 140], [1000, 230], 10) 
    pygame.draw.line(screen, RED, [0, 150], [1000, 240], 10) 
    pygame.draw.line(screen, GREEN, [0, 160], [1000, 250], 10) 
    pygame.draw.line(screen, RED, [0, 170], [1000, 260], 10) 
    pygame.draw.line(screen, GREEN, [0, 180], [1000, 270], 10) 
    pygame.draw.line(screen, RED, [0, 190], [1000, 280], 10) 
    pygame.draw.line(screen, GREEN, [0, 200], [1000, 290], 10) 
    pygame.draw.line(screen, RED, [0, 210], [1000, 300], 10) 
    pygame.draw.line(screen, GREEN, [0, 220], [1000, 310], 10)    
    pygame.draw.line(screen, RED, [0, 230], [1000, 320], 10) 
    pygame.draw.line(screen, GREEN, [0, 240], [1000, 330], 10)    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
