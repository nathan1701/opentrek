# Draw NAV circle
import pygame
import math




def get_nav(center, color):

        position = pygame.mouse.get_pos()
        angle = math.atan2(position[0] - center[0], position[1] - center[1])
        degrees = 180 - (angle * 57.29)
        degrees = round(degrees, 1)
        font = pygame.font.Font(None, 24)

        degreestext = font.render(str(degrees), True, color)
        textRect = degreestext.get_rect()
        textRect.topright = [center[0], center[1] + 75]

        cosine = math.cos(math.radians(degrees))
        sine = math.sin(math.radians(degrees))
        cosine = round(cosine, 2)
        sine = round(sine, 2)
        adjacent = cosine * 50
        opposite = sine * 50
        adjacent = round(adjacent, 2)
        opposite = round(opposite, 2)
        x_coord = int(opposite)
        y_coord = int(adjacent)
        return x_coord, y_coord, degreestext, textRect




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
surface.blit(debug1text, debug1textRect)
surface.blit(debug2text, debug2textRect)
surface.blit(debug3text, debug3textRect)
'''