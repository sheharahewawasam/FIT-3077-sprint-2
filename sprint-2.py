import pygame
# Initialize Pygame
pygame.init()
# Define colors
BLACK = (0, 0, 0)
# Set up the display
window_size = (824, 642)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Game Board')
unning = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)  # Clear the screen
pygame.quit()  # Clean up
