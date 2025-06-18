import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    

    def draw(self, screen):
        pass


    def update(self, dt):
        pass

    
    def detect_collision(self, target):
        total_radius = self.radius + target.radius
        distance_to_target = self.position.distance_to(target.position)
        if (distance_to_target <= total_radius):
            return True
        else:
            return False
    