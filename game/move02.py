import pygame
import numpy as np
import random
import math


WIDTH, HEIGHT = 800, 600
BG_COLOR = (128, 255, 128)
SURF_COLOR = (100, 200, 200)
SURF2_COLOR = (0, 255, 0)
POINT_COLOR = (255, 0, 0)

RECT_SIZE = (20, 20)
SURFACE_SIZE = (60, 60)
SURFACE2_SIZE = (80, 65)

L_END, R_END = 5, WIDTH - SURFACE_SIZE[0] - 5
T_END, D_END = 5, HEIGHT - SURFACE_SIZE[1] - 5
EDGE_BOUND = [L_END, R_END, T_END, D_END]

BASE_SPEED = 4
HIGH_SPEED = 7

COUNT_THRESH = 20
ROTATE_DEG = 2



def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def rotate_point(x, y, deg):
    theta = math.radians(deg)
    c, s = math.cos(theta), math.sin(theta)
    mat = np.array([[c, -s], [s, c]])
    res = mat @ np.array([x, y], dtype=float)
    return float(res[0]), float(res[1])

def clamp_rect_within_bounds(rect, left, right, top, bottom):
    rect.x = max(left, min(rect.x, right))
    rect.y = max(top, min(rect.y, bottom))

def collision_threshold(rect_a, rect_b):
    
    ra = math.sqrt((rect_a.width / 2) ** 2 + (rect_a.height / 2) ** 2)
    rb = math.sqrt((rect_b.width / 2) ** 2 + (rect_b.height / 2) ** 2)
    return ra + rb + 3  



class Fracturer:
    def __init__(self):
        self.used_x = set()
        self.points_drawn = 0

    def draw(self, surface, max_points=COUNT_THRESH):
        if self.points_drawn >= max_points:
            return
        x = random.randint(10, surface.get_width() - 10)

        attempts = 0
        while x in self.used_x and attempts < 10:
            x = random.randint(10, surface.get_width() - 10)
            attempts += 1
        self.used_x.add(x)

        y = random.randint(10, surface.get_height() - 10)
        pygame.draw.circle(surface, POINT_COLOR, (x, y), 2)
        self.points_drawn += 1



class Player:
    def __init__(self, pos):
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.surface.fill(SURF_COLOR)
        self.rect = pygame.Rect(pos[0], pos[1], *RECT_SIZE)
       

    def handle_input(self, keys):
  
        if keys[pygame.K_a] and self.rect.x > L_END:
            self.rect.x -= HIGH_SPEED if keys[pygame.K_RSHIFT] else BASE_SPEED
        if keys[pygame.K_d] and self.rect.x < R_END:
            self.rect.x += HIGH_SPEED if keys[pygame.K_RSHIFT] else BASE_SPEED
 
        if keys[pygame.K_w] and self.rect.y > T_END:
            self.rect.y -= HIGH_SPEED if keys[pygame.K_RSHIFT] else BASE_SPEED
        if keys[pygame.K_s] and self.rect.y < D_END:
           
            self.rect.y += HIGH_SPEED if not keys[pygame.K_RSHIFT] else BASE_SPEED

        if keys[pygame.K_RCTRL]:
            x, y = rotate_point(self.rect.x, self.rect.y, ROTATE_DEG)
            self.rect.x, self.rect.y = int(x), int(y)

        clamp_rect_within_bounds(self.rect, L_END, R_END, T_END, D_END)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

class Box:
    def __init__(self, pos, size=SURFACE2_SIZE, color=SURF2_COLOR):
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.rect = pygame.Rect(pos[0], pos[1], size[0] // 3, size[1] // 3)  
        self.fracturer = Fracturer()

    def jiggle(self):
        pass

    def fracture_on_collision(self):
        self.fracturer.draw(self.surface)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

class DotBox:
    def __init__(self, pos, size=(10, 10)):
        self.surface = pygame.Surface(size)
        self.surface.fill((200, 200, 0))
        self.rect = pygame.Rect(pos[0], pos[1], *size)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(pos=(0, 400))
    box = Box(pos=(300, 200))
    dot_box = DotBox(pos=(300, 500))

    running = True
    is_collide = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.rect.y = max(T_END, player.rect.y - 10)

        keys = pygame.key.get_pressed()

    
        player.handle_input(keys)
        box.jiggle()

      
        center_player = player.rect.center
        center_box = box.rect.center
        dist = distance(center_player, center_box)
        thresh = collision_threshold(player.rect, box.rect)

        if dist <= thresh:
            is_collide = True
          
            x, y = rotate_point(player.rect.x, player.rect.y, ROTATE_DEG)
            player.rect.x, player.rect.y = int(x), int(y)
        else:
            is_collide = False

  
        screen.fill(BG_COLOR)
        if is_collide:
            box.fracture_on_collision()

        player.draw(screen)
        box.draw(screen)
        dot_box.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
