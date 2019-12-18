from var import *
from random import randint
from OpenGL.GL import glBegin, glEnd, glVertex2dv, GL_QUADS, glColor3ubv
from math import sqrt

class Quad:
    def __init__(self,x,y,i_x,i_y,smer=[0,0]):
        self.x=x
        self.y=y
        self.i_x=i_x
        self.i_y=i_y
        self.smer=smer
        self.color=(randint(50,200),randint(50,200),randint(50,200))
        self.size=QUAD_SIZE
        self.vertex=[[self.x-self.size,self.y-self.size],[self.x+self.size,self.y-self.size],[self.x+self.size,self.y+self.size],[self.x-self.size,self.y+self.size]]

    def update_vertex(self):
        self.vertex=[[self.x-self.size,self.y-self.size],[self.x+self.size,self.y-self.size],[self.x+self.size,self.y+self.size],[self.x-self.size,self.y+self.size]]

    def move(self):
        self.x+=self.smer[0]
        self.y+=self.smer[1]

    def draw(self):
        glBegin(GL_QUADS)
        glColor3ubv(self.color)
        for i in self.vertex:
            glVertex2dv(i)
        glEnd()
        self.update_vertex()

    def __sub__(self, other):
        if sqrt(pow(self.smer[0],2)+pow(self.smer[1],2))>sqrt(pow(other.smer[0],2)+pow(other.smer[1],2)):
            return [self.smer[0]-other.smer[0],self.smer[1]-other.smer[1]]
        else:
            return [other.smer[0]-self.smer[0],other.smer[1]-self.smer[1]]