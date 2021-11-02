import pygame,sys
import random

from pygame.transform import rotate

# Initialize game
pygame.init()
clock = pygame.time.Clock()



#Screen
screen = pygame.display.set_mode((800,800))
notch = pygame.image.load('notch.png')
notch_rect = notch.get_rect(center = (400,0))

#spinning wheel
wheel = pygame.image.load('Circle.png')
wheel_rect = wheel.get_rect(center = (400,350))

#angles
angles = [45,45,90,135,180,225,270,315]
randomAngle = random.choice(angles)
currentAngle = 0

print(randomAngle)

def RotateWheel(surface,angle):
    rotated_surface = pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center=(400,350))

    return rotated_surface,rotated_rect


#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if(currentAngle<randomAngle):
        currentAngle+=1
    
    else:
        currentAngle = randomAngle

    


    


    screen.fill((255,255,255))
    screen.blit(notch,notch_rect)

    circle_rotated,circle_rotated_rect = RotateWheel(wheel,currentAngle)
    screen.blit(circle_rotated,circle_rotated_rect)

    pygame.display.flip()
    clock.tick(60)