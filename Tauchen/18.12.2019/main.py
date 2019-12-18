import window
from random import randint
from quad import Quad
from pygame.display import flip
from pygame.time import Clock
from OpenGL.GL import *
from var import *

window.window()
events=window.event_hendler
fps=Clock()
quads=[]
quads_x={}
quads_y={}
for i in range(QUAD_SPAWN):
    quads.append(Quad(randint(-960+QUAD_SIZE,960-QUAD_SIZE),randint(-540+QUAD_SIZE,540-QUAD_SIZE),i,i,[randint(-10000,10000)/10000,randint(-10000,10000)/10000]))
    quads_x.update({i:quads[i].x})
    quads_y.update({i:quads[i].y})

'''def check_colisions(quads,quads_x,quads_y):
    for quad in quads:
        if quad.x+QUAD_SIZE<=list(quads_x.values())[quad.i_x+1] or quad.x-QUAD_SIZE<=list(quads_x.values())[quad.i_x-1]:
            pass
        if quad.y+QUAD_SIZE<=list(quads_y.values())[quad.i_y+1] or quad.y-QUAD_SIZE<=list(quads_y.values())[quad.i_y-1]:
            pass'''




def check_border(quads,quad_x_min,quad_x_max,quad_y_min,quad_y_max):
    if quads[quad_x_min].x<=-960+QUAD_SIZE:
        quads[quad_x_min].smer[0] = -quads[quad_x_min].smer[0]
        quads[quad_x_min].move()
    if quads[quad_x_max].x>=960-QUAD_SIZE:
        quads[quad_x_max].smer[0] = -quads[quad_x_max].smer[0]
        quads[quad_x_max].move()
    if quads[quad_y_min].y<=-540+QUAD_SIZE:
        quads[quad_y_min].smer[1] = -quads[quad_y_min].smer[1]
        quads[quad_y_min].move()
    if quads[quad_y_max].y>=540-QUAD_SIZE:
        quads[quad_y_max].smer[1] = -quads[quad_y_max].smer[1]
        quads[quad_y_min].move()

def sort_x(quads_x):
    return {key: value for key, value in sorted(quads_x.items(), key=lambda item: item[1])}

def sort_y(quads_y):
    return {key: value for key, value in sorted(quads_y.items(), key=lambda item: item[1])}

def update(quads, quads_x, quads_y):
    quads_x = {}
    quads_y = {}
    for i in range(QUAD_SPAWN):
        quads_x.update({i: quads[i].x})
        quads_y.update({i: quads[i].y})
    quads_x=sort_x(quads_x)
    quads_y=sort_y(quads_y)
    return (quads_x, quads_y)

def draw():
    for quad in quads:
        quad.draw()
    flip()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

while True:
    events()
    draw()
    for quad in quads:
        quad.move()
        quads_x, quads_y=update(quads,quads_x,quads_y)
    check_border(quads,int(list(quads_x.keys())[0]),int(list(quads_x.keys())[len(quads_x)-1]),int(list(quads_y.keys())[0]),int(list(quads_y.keys())[len(quads_y)-1]))
    fps.tick(120)