class Settings:
    """Class to store all settings for Alien Invasion."""
    def __init__(self):
        #Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (212, 246, 250)
        
        #Ship settings
        self.ship_speed = 2.5
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Direction 1 is right and direction -1 is left
        self.fleet_direction = 1