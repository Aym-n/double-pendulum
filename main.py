
import pygame
import math


#Leength Of Strings
r1 = 200;
r2 = 200;

#Mass of Pendulum Bobs
m1 = 10;
m2 = 10;

#Intial Angle
a1 = math.pi/2; 
a2 = math.pi/2;

#Angular Velocities
v1 = 0;
v2 = 0;

#Angular Accelaration
accel1 = 0;
accel2 = 0;

#Accleration Due to Gravity
g = 1;

#Coefficent to simulate Viscousity
damping = 0.999;

#length of trailing points
lineLength = 50;
lineColor = (6, 120, 200);

def transformCoords(x, y):
    return (x + 450, y + 150)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Double Pendulum")

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
        
        
    screen.fill((29, 30, 31))
    
    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * m2 * ((v2 * v2) * r2 + (v1 * v1) * r1 * math.cos(a1 - a2))
    den1 = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

    accel1 = (num1 + num2 + num3) / den1

    num4 = 2 * math.sin(a1 - a2)
    num5 = (v1 * v1) * r1 * (m1 + m2)
    num6 = g * (m1 + m2) * math.cos(a1)
    num7 = (v2 * v2) * r2 * m2 * math.cos(a1 - a2)
    den2 = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

    accel2 = (num4 * (num5 + num6 + num7)) / den2

    v1 += accel1
    v2 += accel2

    a1 += v1
    a2 += v2

    x1 = r1 * math.sin(a1)
    x2 = x1 + r2 * math.sin(a2)

    y1 = r1 * math.cos(a1)
    y2 = y1 + r2 * math.cos(a2)

    points.append(transformCoords(x2, y2))

    if len(points) > lineLength:
        points.pop(0)

    pygame.draw.lines(screen, lineColor, False, points , 1)

    pygame.draw.line(screen, (100, 100, 100), transformCoords(0, 0), transformCoords(x1, y1))
    pygame.draw.line(screen, (100, 100, 100), transformCoords(x1, y1), transformCoords(x2, y2))
    pygame.draw.circle(screen, (6, 143, 255), transformCoords(x1, y1), m1)
    pygame.draw.circle(screen, (6, 143, 255), transformCoords(x2, y2), m2)
    
    v1 *= damping
    v2 *= damping

    pygame.display.flip()

    clock.tick(60)

pygame.quit()