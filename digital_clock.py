import pygame
import sys
import datetime
import pytz

# Initialize Pygame
pygame.init()

# Set up constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 48

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Digital Clock')

# Set up fonts
font = pygame.font.Font(None, FONT_SIZE)

# Define time zones
TIMEZONES = {
    'UTC': pytz.utc,
    'US/Pacific': pytz.timezone('US/Pacific'),
    'US/Eastern': pytz.timezone('US/Eastern'),
    'Europe/London': pytz.timezone('Europe/London'),
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    for idx, (zone_name, tz) in enumerate(TIMEZONES.items()):
        # Get the current time in the specific timezone
        local_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        text = f'{zone_name}: {local_time}'
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50 + idx * 60))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()