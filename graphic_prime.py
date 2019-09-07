import pygame
from time import process_time

file = open('prime_data.txt')
prime = file.read().strip().split("\n")
file.close()

pygame.init()

class Dimension():
    def __init__(self,dimension,dim_screen):
        self.case = dimension
        self.iteration = (dim_screen / dimension) ** 2
        self.screen = [dim_screen,dim_screen]

class Case(pygame.sprite.Sprite):
    def __init__(self,color,co):
        super(Case, self).__init__()
        self.surf = pygame.Surface((dim.case,dim.case))
        self.color = color
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        self.co = co

class Variable():
    def __init__(self):
        self.cases = []
        self.total_number = 1
        self.coordonate = [(dim.screen[0]/2)/dim.case,(dim.screen[0]/2)/dim.case]
        self.last_found = 0

dim = Dimension(3,3000)

screen = pygame.display.set_mode(dim.screen)

running = True
color1 = (255,255,255)
color2 = (65,105,225)
v = Variable()

def go_left(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        if i != number -1:
            v.coordonate[0] -= 1
        v.total_number += 1

def go_right(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        if i != number -1:
            v.coordonate[0] += 1
        v.total_number += 1

def go_high(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        if i != number -1:
            v.coordonate[1] -= 1
        v.total_number += 1

def go_down(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        v.total_number += 1
        if i != number - 1:
            v.coordonate[1] += 1

def go_diagonal(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        v.total_number += 1
        if i != number - 1:
            v.coordonate[1] += 1
            v.coordonate[0] += 1

def go_diagonal2(number,color1,color2):
    for i in range(number):
        if control_prime(v.total_number,prime):
            v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
        else:
            v.cases.append(Case(color1,[v.coordonate[0], v.coordonate[1]]))
        v.total_number += 1
        if i != number - 1:
            v.coordonate[1] -= 1
            v.coordonate[0] += 1

def control_prime(number,prime):
    i = v.last_found
    while int(prime[i]) <= number:
        if number == int(prime[i]):
            v.last_found = i
            return False
        i += 1
    return True

def construct_spiral():
    path_lenght = 2
    v.cases.append(Case(color2,[v.coordonate[0], v.coordonate[1]]))
    v.total_number += 1
    v.coordonate[1] -= 1 
    go_left(path_lenght,color1,color2)
    v.coordonate[1] += 1
    go_down(path_lenght,color1,color2)
    v.coordonate[0] += 1
    go_right(path_lenght,color1,color2)
    v.coordonate[1] -= 1
    path_lenght += 1
    go_high(path_lenght,color1,color2)
    v.coordonate[0] -= 1
    while v.total_number < dim.iteration:
        go_left(path_lenght,color1,color2)
        v.coordonate[1] += 1
        path_lenght += 1
        go_down(path_lenght,color1,color2)
        v.coordonate[0] += 1
        go_right(path_lenght,color1,color2)
        v.coordonate[1] -= 1
        path_lenght += 1
        go_high(path_lenght,color1,color2)
        v.coordonate[0] -= 1

def display_background(cases):
    for i in range(len(cases)):
        screen.blit(cases[i].surf,(dim.case * cases[i].co[0],dim.case * cases[i].co[1]))

def construct_line():
    v.coordonate[0] = 0
    v.coordonate[1] = 0
    while v.total_number < dim.iteration:
        print(int((dim.screen[0] / 2) / dim.case))
        go_right(int((dim.screen[0]) / dim.case),color1,color2)
        v.coordonate[1] += 1
        v.coordonate[0] = 0

def construct_diagonal():
    v.coordonate[0] = 0
    v.coordonate[1] = 0
    co_x = 0
    co_y = 0
    nbre = 0
    go_diagonal(int((dim.screen[0]) / dim.case),color1,color2)
    while v.total_number < dim.iteration:
        nbre += 1
        co_x += 1
        v.coordonate[0] = co_x
        v.coordonate[1] = 0
        go_diagonal(int((dim.screen[0]) / dim.case) - nbre,color1,color2)
        co_y += 1
        v.coordonate[1] = co_y
        v.coordonate[0] = 0
        go_diagonal(int((dim.screen[0]) / dim.case) - nbre,color1,color2)

def construct_diagonal2():
    v.coordonate[0] = 0
    v.coordonate[1] = 0
    go_diagonal2(1,color1,color2)
    iteration = 1
    co_y = 0
    co_x = 0
    while v.total_number <= dim.iteration:
        if co_y < dim.screen[0] / dim.case - 1:
            iteration += 1
            co_y += 1
            v.coordonate[1] = co_y
            v.coordonate[0] = 0
            go_diagonal2(iteration,color1,color2)
        else: 
            iteration -= 1
            co_x += 1
            v.coordonate[1] = co_y
            v.coordonate[0] = co_x
            go_diagonal2(iteration,color1,color2)


#construct_spiral()
construct_line()
#construct_diagonal()
#construct_diagonal2()

done = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not done:
        print(process_time())
        done = True
    display_background(v.cases)
    pygame.display.flip()
