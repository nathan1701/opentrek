import math
import pygame
import random
import navcircle

# Let's import the Car Class
from car import Car
from ship import Ship

pygame.init()
navcenter = [1500, 450]
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

clicks = None

SCREENWIDTH = 1600
SCREENHEIGHT = 900

XCOORD = 0
YCOORD = 0
previousXCOORD = 0
previousYCOORD = 0

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Star Trek")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

player1 = Ship('enterprise', 'federationHC')
player1.rect.x = 500
player1.rect.y = 500
player2 = Ship('koplah', 'defiant')

playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = -100

car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(CYAN, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300
car4 = Car(BLUE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
all_sprites_list.add(player1)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

# Allowing the user to close the window...
carryOn = True
clock = pygame.time.Clock()

'''
menu = pygame_menu.Menu(300,400,'Select Ship',theme=pygame_menu.themes.THEME_DARK)
menu.add_text_input('Name:', default='Starship')
menu.add_selector('Model:',['enterpriseA','bird-of-prey'], onchange=Ship()
#menu.add_button('play', start_the_game())
menu.mainloop(screen)
'''
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        # elif event.type==pygame.KEYDOWN:
        # if event.key==pygame.K_x:
        # playerCar.moveRight(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05
    if keys[pygame.K_m]:
        command = 'move'
    clicks = pygame.mouse.get_pressed()



    # Game Logic
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSpeed(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200

    all_sprites_list.update()

    # Drawing on Screen
    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, navcenter, 50, 1)

    if clicks[2]:
        XCOORD, YCOORD, degreestext, textRect = navcircle.get_nav(navcenter,GREEN)
        pygame.draw.circle(screen, GREEN, [navcenter[0] + XCOORD, navcenter[1] - YCOORD], 5, 0)
        screen.blit(degreestext, textRect)
        pygame.draw.circle(screen, GREEN, [navcenter[0] + previousXCOORD, navcenter[1] - previousYCOORD], 5, 0)
    else:
        pygame.draw.circle(screen, GREEN, [navcenter[0] + previousXCOORD, navcenter[1] - previousYCOORD], 5, 0)
        previousYCOORD = YCOORD
        previousXCOORD = XCOORD

    # Debug variables and labels to print in top right corner.
    '''
    debug1 = cosine
    debug2 = ycoord
    debug3 = xcoord
    debug1_label = "cosine"
    debug2_label = "adjacent"
    debug3_label = "opposite"
    debug1text = font.render((debug1_label + " " + str(debug1)), True, GREEN)
    debug2text = font.render((debug2_label + " " + str(debug2)), True, GREEN)
    debug3text = font.render((debug3_label + " " + str(debug3)), True, GREEN)
    debug1textRect = debug1text.get_rect()
    debug2textRect = debug2text.get_rect()
    debug3textRect = debug3text.get_rect()
    debug1textRect.topright = [1550, 10]
    debug2textRect.topright = [1550, 40]
    debug3textRect.topright = [1550, 70]
    screen.blit(debug1text, debug1textRect)
    screen.blit(debug2text, debug2textRect)
    screen.blit(debug3text, debug3textRect)
'''
    #screen.blit(player1.image, [500, 500])
    screen.blit(player2.image, [600, 600])

    # Draw The Road
    pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])

    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()


    # Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()
