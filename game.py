# game.py
# The main worldBuilder game file
# (c) 2016 Matthew Filmer

import sys

import pygame
from dwarf import Dwarf
import ai

screen = pygame.display.set_mode((640,480))
dwarfSkin = pygame.image.load('images/dwarf.png').convert()
dwarfSkin.set_colorkey((255,0,255))

background = 255, 255, 255

allDwarves = pygame.sprite.LayeredDirty()

for i in range(1,3):
    newDwarf = Dwarf()
    newDwarf.setSkin(dwarfSkin)
    newDwarf.setAi(ai.Wander)
    allDwarves.add(newDwarf)

# Initial drawing
screen.fill(background)
dirtyRects = allDwarves.draw(screen)
pygame.display.update(dirtyRects)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    allDwarves.update(1)
    
    screen.fill(background)
    dirtyRects = allDwarves.draw(screen)
    pygame.display.update(dirtyRects)
