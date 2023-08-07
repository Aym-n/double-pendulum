
import pygame
import math

r1 = 200;
r2 = 200;
m1 = 10;
m2 = 10;
a1 = math.pi/2;
a2 = 0;
g = 1;

v1 = 0;
v2 = 0;

accel1 = 0;
accel2 = 0;

def transformCoords(x, y):
    return (x + 300, y)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

x1 = r1 * math.sin(a1)
x2 = x1 + r2 * math.sin(a2)

y1 = r1 * math.cos(a1)
y2 = y1 + r2 * math.cos(a2)


points = [(x2, y2)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
    screen.fill((0, 0, 0))

    a1 += v1
    a2 += v2

    v1 += accel1
    v2 += accel2

    dx1 = -g * (2 * m1 + m2) * math.sin(a1) - m2 * g * math.sin(a1 - 2 * a2) - 2 * math.sin(a1 - a2) * m2 * (v2 * v2 * r2 + v1 * v1 * r1 * math.cos(a1 - a2)) / (r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2)))

    dx2 = 2 * math.sin(a1 - a2) * (v1 * v1 * r1 * (m1 + m2) + g * (m1 + m2) * math.cos(a1) + v2 * v2 * r2 * m2 * math.cos(a1 - a2)) / (r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2)))


    pygame.draw.line(screen, (255, 255, 255), transformCoords(0, 0), transformCoords(x1, y1))
    pygame.draw.line(screen, (255, 255, 255), transformCoords(x1, y1), transformCoords(x2, y2))
    pygame.draw.circle(screen, (255, 255, 255), transformCoords(x1, y1), m1)
    pygame.draw.circle(screen, (255, 255, 255), transformCoords(x2, y2), m2)
    
    

    a1 += 0.1
    a2 -= 0.02

    points.append(transformCoords(x2, y2))

    if len(points) > 10:
        points.pop(0)

    pygame.draw.lines(screen, (255, 255, 255), False, points , 1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()