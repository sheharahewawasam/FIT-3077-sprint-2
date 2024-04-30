import pygame
import math
# Initialize Pygame
pygame.init()
# Define colors
BLACK = (0, 0, 0)
ICON_COLORS = {
    'token_1': (255, 0, 0),  # Red tokens
    'token_2': (0, 255, 0),  # Green tokens
}
font = pygame.font.Font(None, 36)
# Set up the display
window_size = (824, 642)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Game Board')
# Function to draw a rhombus
def draw_rhombus(center_x, center_y, width, height, color, text=''):
    points = [
        (center_x, center_y - height // 2),  # Top point
        (center_x + width // 2, center_y),   # Right point
        (center_x, center_y + height // 2),  # Bottom point
        (center_x - width // 2, center_y),   # Left point
    ]
    pygame.draw.polygon(screen, color, points)
    if text:
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(center_x, center_y))
        screen.blit(text_surface, text_rect)
# Function to draw the board
def draw_board():
    tiles_per_row = 7 # Increased size to allow for a border
    tiles_per_row_inner = 4
    rhombus_width = 50  # The width of each rhombus
    rhombus_height = 50  # The height of each rhombus
    spacing_width = -10  # Spacing between rhombuses
    spacing_height = 20  # Spacing between rhombuses

    cos_theta = math.cos(math.radians(45))
    sin_theta = math.sin(math.radians(45))

    # Calculate the starting point for the very top of the rhombus board, before rotation
    start_x = window_size[0] // 2
    start_y = window_size[1] // 2.5
    start_x_inner = window_size[0] // 2
    start_y_inner = window_size[1] // 1.9
    # Draw the rhombuses for the board
    for row in range(tiles_per_row):
        for col in range(tiles_per_row):
            if row == 0 or row == tiles_per_row - 1 or col == 0 or col == tiles_per_row - 1:
                # Original center coordinates before rotation
                original_x = (col * (rhombus_width + spacing_width*cos_theta)) - (tiles_per_row * (rhombus_width + spacing_width*cos_theta)) // 4
                original_y = (row * (rhombus_height // 2 + spacing_height*sin_theta)) - (tiles_per_row * (rhombus_height // 2 + spacing_height*sin_theta)) // 4

                # Rotated coordinates
                center_x = int(start_x + original_x * cos_theta - original_y * sin_theta)
                center_y = int(start_y + original_x * sin_theta + original_y * cos_theta)


                # Alternate colors based on column and row for a checkered pattern
                color = ICON_COLORS['token_2'] 
                draw_rhombus(center_x, center_y, rhombus_width, rhombus_height, color)
    for row in range(tiles_per_row_inner):
        for col in range(tiles_per_row_inner):
            # Original center coordinates before rotation
            original_x_inner = (col * (rhombus_width + spacing_width)) - (tiles_per_row * (rhombus_width + spacing_width)) // 4
            original_y_inner = (row * (rhombus_height // 2 + spacing_height)) - (tiles_per_row * (rhombus_height // 2 + spacing_height)) // 4
            
            # Rotated coordinates
            center_x_inner = int(start_x_inner + original_x_inner * cos_theta - original_y_inner * sin_theta)
            center_y_inner = int(start_y_inner + original_x_inner * sin_theta + original_y_inner * cos_theta)
            
            # Alternate colors based on column and row for a checkered pattern
            color = ICON_COLORS['token_1'] 
            draw_rhombus(center_x_inner, center_y_inner, rhombus_width, rhombus_height, color)
            
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)  # Clear the screen
pygame.quit()  # Clean up
