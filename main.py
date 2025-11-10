import pygame
import time

#equation
a,b,c = 3,5,10 #f(x) = ax^2 + bx + c

width, height = 1500, 800
unit_size = 10
origin = width//2, height//2
grid_color = (50,50,50)
pygame.init()
fps = 30 #in ms(miliseconds)
screen = pygame.display.set_mode((width, height))

def draw():
    print(origin)
    screen.fill((0,0,0))
    
    for i in range(height//unit_size):
        pygame.draw.rect(screen, grid_color, (0 ,unit_size*i, width,1))
    for j in range(width//unit_size):
        pygame.draw.rect(screen, grid_color, (unit_size*j ,0, 1,height))

    pygame.draw.line(screen, (255,255,255), (0,origin[1]), (width, origin[1]))
    pygame.draw.line(screen, (255,255,255), (origin[0], 0), (origin[0], height))

    for i in range(0, width):
        x1 = origin[0] + i
        y1 = origin[1] + a*((i/unit_size)**2) + b*(i/unit_size) + c

        x2 = origin[0] + (i+1)
        y2 = origin[1] + a*(((i+1)/unit_size)**2) + b*((i+1)/unit_size) + c
        
        pygame.draw.line(screen, (255,0,0), (x1,y1), (x2,y2))

    pygame.display.update()

x1,y1,x2,y2 = 0,0,0,0
mouse = 0
draw()
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse = 1
            x1,y1 = pygame.mouse.get_pos()
        if(event.type == pygame.MOUSEBUTTONUP):
            mouse = 0
            x2,y2 = pygame.mouse.get_pos()
            origin = (origin[0]+(x2-x1), origin[1]+y2-y1)
            origin = (origin[0]//unit_size * unit_size, origin[1]//unit_size * unit_size)
            draw()
    time.sleep(1/fps)
