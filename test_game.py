import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load gif image
background_image = pygame.image.load('water.gif')

# Set the size for the gif image
DEFAULT_IMAGE_SIZE = (1000, 1000)
background_image = pygame.transform.scale(background_image, DEFAULT_IMAGE_SIZE)

# Load image
ship_image = pygame.image.load('ship.png')

# Set the size for the ship image
DEFAULT_SHIP_SIZE = (200, 200)
ship_image = pygame.transform.scale(ship_image, DEFAULT_SHIP_SIZE)

# Set adjusted initial positions for each ship
ship_positions = [
    (100, 100),               # Top-left corner
    (width - 300, 100),        # Top-right corner
    (width - 300, height - 300),   # Bottom-right corner
    (100, height - 300)       # Bottom-left corner
]

# Initial rotation angles for each ship
rotation_angles = [0, 0, 0, 0]

# Prepare loop condition
running = True

# Event loop
while running:

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Show the gif image as the background
    screen.blit(background_image, (0, 0))

    # Iterate through each ship
    for i in range(4):
        # Rotate the ship image by the current rotation angle for each ship
        rotated_ship_image = pygame.transform.rotate(ship_image, rotation_angles[i])

        # Get the rect of the rotated ship image and set its center to the corresponding position
        rect = rotated_ship_image.get_rect(center=ship_positions[i])

        # Show the rotated ship image for each ship
        screen.blit(rotated_ship_image, rect.topleft)

        # Update rotation angle for the next iteration for each ship
        rotation_angles[i] += 1  # You can adjust the rotation speed by changing this value

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
