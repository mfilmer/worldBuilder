# game.py
# The main worldBuilder game file
# (c) 2016 Matthew Filmer

import sys

import pygame
from dwarf import Dwarf

screen = pygame.display.set_mode((640,480))
dwarfSkin = pygame.image.load('images/dwarf.png').convert()

background = 255, 255, 255

allDwarves = pygame.sprite.LayeredDirty()
dwarf1 = Dwarf()
dwarf1.setSkin(dwarfSkin)
allDwarves.add(dwarf1)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        screen.fill(background)
        dirtyRects = allDwarves.draw(screen)
        pygame.display.update(dirtyRects)
