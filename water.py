import pygame, random

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()
run = True

world = [[0 for x in range(40)] for i in range(40)]
world[10][10] = 1
world[39][10] = 1
world[0][0] = 1
world[39 - 1][39 - 1] = 1

moused = False


def gridlines():
    [pygame.draw.line(DISPLAY, "gray", (0, i * 20), (800, i * 20)) for i in range(40)]
    [pygame.draw.line(DISPLAY, "gray", (i * 20, 0), (i * 20, 800)) for i in range(40)]
    
def water():
    for i in range(40 - 1, -1, -1):
        for j in range(40 - 1, -1, -1):
            #presand
            if world[i][j]:
                if i < 39 and not world[i + 1][j]:
                    world[i][j] = 0
                    world[i + 1][j] = 1
                    
            #flowsides
            if world[i][j]:
                if i < 39 and world[i + 1][j]:
                    for x in range(j, -1, -1):
                        if not world[i + 1][x]:
                            world[i][j] = 0
                            world[i + 1][x] = 1
                            break
                    for x in range(j, 40):
                        if not world[i + 1][x]:
                            world[i][j] = 0
                            world[i + 1][x] = 1
                            break
                            
            # sides
            # r_sides = random.randrange(0, 2)
            # if world[i][j]:
                # if j > 0 and not r_sides and not world[i][j - 1]:
                    # world[i][j] = 0
                    # world[i][j - 1] = 1
            # if world[i][j]:
                # if j < 39 and r_sides and not world[i][j + 1]:
                    # world[i][j] = 0
                    # world[i][j + 1] = 1  
    
    for i in range(40):
        for j in range(40):
            test_rect = pygame.Rect(j * 20, i * 20, 20, 20)
            mousex, mousey = pygame.mouse.get_pos()
            if moused:
                if abs(test_rect.center[0] - mousex) <= 10 and abs(test_rect.center[1] - mousey) <= 10:
                    world[i][j] = 1 
    
    for i in range(40):
        for j in range(40):
            if world[i][j]:
                pygame.draw.rect(DISPLAY, "lightblue", (j * 20, i * 20, 20, 20))

while run:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moused = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moused = False
            
    key = pygame.key.get_pressed()
    
    DISPLAY.fill("black")
    
    water()
    
    # gridlines()
    
    pygame.display.update()
    
pygame.quit()