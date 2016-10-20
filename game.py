# game.py
# The main worldBuilder game file
# (c) 2016 Matthew Filmer

import sys

import pygame
from dwarf import Dwarf
from block import Wood,Stone,Dirt
import ai

screen = pygame.display.set_mode((640,480))
dwarfSkin = pygame.image.load('images/dwarf.png').convert()
dwarfSkin.set_colorkey((255,0,255))

background = 255, 255, 255

# Create the world
worldBlocks = pygame.sprite.Group()
for x in range(0,640,10):
    for y in range(50,100,10):
        newBlock = Dirt((x,y))
        worldBlocks.add(newBlock)
    for y in range(100,400,10):
        newBlock = Stone((x,y))
        worldBlocks.add(newBlock)

# Create the Dwarves
allDwarves = pygame.sprite.Group()
for i in range(1,3):
    newDwarf = Dwarf()
    newDwarf.setSkin(dwarfSkin)
    newDwarf.setAi(ai.Wander)
    allDwarves.add(newDwarf)

# Create group to hold all drawables
allDrawables = pygame.sprite.LayeredDirty()
allDrawables.add(worldBlocks)
allDrawables.add(allDwarves)

# Initial drawing
screen.fill(background)
dirtyRects = allDrawables.draw(screen)
pygame.display.update(dirtyRects)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    allDwarves.update(1)
    worldBlocks.update()
    
    screen.fill(background)
    dirtyRects = allDrawables.draw(screen)
    pygame.display.update(dirtyRects)
