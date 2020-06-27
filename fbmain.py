import pygame
import os
from time import sleep

pygame.init()

font_big = pygame.font.Font(None, 64)
lcd = pygame.display.set_mode((1120, 600))
pygame.mouse.set_visible(False)
lcd.fill((80, 80, 70))
pygame.display.update()
fullname = os.path.join('.\sprites', "bananat.png")
image = pygame.image.load(fullname)
lcd.blit(image, (1, 50))
pygame.display.flip()
print(pygame.display.get_driver())
print(pygame.display.Info())

for x in range(1, 900, +2):
    sleep(0.004)
    lcd.fill((80, 80, 80))
    lcd.blit(image, (x, 50))
    lcd.blit(image, (900 - x, 220))
    pygame.display.update()
    #pygame.display.flip()

exit(3)