import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initalize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship3.bmp") #Load ship image and get its rect.
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #Start each new ship at the bottom center.
        self.x = float(self.rect.x) #Store a float for the ship's exact horizontal position
        #Movement flags, start with ship that's not moving.
        self.moving_right = False 
        self.moving_left = False 
        

    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x #Update rect object from self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)