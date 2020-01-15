import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from math import sin,cos, pi
from random import randint as ri
from os import environ



WINDOW_SIZE = (1920,1080)
MSAA        = 16

NODE_SPAWN  = 500

COLOR_FADE  = 20

CLOCKWISE   = -1

def window():
    environ['SDL_VIDEO_CENTERED']="1"
    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE,pygame.DOUBLEBUF|pygame.OPENGL|pygame.NOFRAME)
    if MSAA:
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS,1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES,MSAA)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,WINDOW_SIZE[0]/WINDOW_SIZE[1],0.1,1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0,10,-250)
    glRotatef(330,0,0,1)
    glRotatef(25,1,0,0)
    pygame.mouse.set_visible(False)
def events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.__dict__.get("key")==pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.__dict__.get("key")==pygame.K_c:
                if globals()["CLOCKWISE"] == -1:
                    globals()["CLOCKWISE"] = 1
                else:
                    globals()["CLOCKWISE"] = -1

class Trait:
    def __init__(self,d,x,y,z,qs,color):
        self.x=x
        self.y=y
        self.z=z
        self.qs=qs
        self.smer=(cos(d),0,sin(d))
        self.color=list(color)
        self.matrix=()
        self.move()

    def move(self):
        self.x+=self.smer[0]
        self.y+=self.smer[1]
        self.z+=self.smer[2]
        for color in self.color:
            if color>0:
                color-=globals().get("COLOR_FADE")
        self.update()

    def update(self):
        self.matrix=(
            (self.x-self.qs,self.y-self.qs,self.z),
            (self.x+self.qs,self.y-self.qs,self.z),
            (self.x+self.qs,self.y+self.qs,self.z),
            (self.x-self.qs,self.y+self.qs,self.z)
        )

    def __call__(self, *args, **kwargs):
        glBegin(GL_QUADS)
        glColor3ubv(self.color)
        for vertex in self.matrix:
            glVertex3dv(vertex)
        glEnd()

class Node:
    def __init__(self,r,y,s,d,qs,color):
        self.r=r #Polomer
        self.y=y #Vyska
        self.s=s #Ryhlost
        self.d=d #Pocatecni stupen
        self.od=d #Pocatecni stupen kopie
        self.qs=qs #Velikost Nody
        self.color=color #Barva
        self.x=0 #Absolutni souradnice X
        self.z=0 #Absolutni souradnice Z
        self.traits=[]
        self.matrix=()
        self.xz()

    def move(self):
        self.d+=self.s*globals()["CLOCKWISE"]
        if self.d<=self.od-2*pi or self.d>=self.od+2*pi:
            self.d=self.od
        self.xz()

    def xz(self):
        self.x=cos(self.d)*self.r
        self.z=sin(self.d)*self.r
        #self.traits.append(Trait(self.d,self.x,self.y,self.z,0.1,self.color))
        #if len(self.traits) > 10:
        #    self.traits.pop(0)
        self.update()

    def update(self):
        self.matrix=(
            (self.x-self.qs,self.y-self.qs,self.z),
            (self.x+self.qs,self.y-self.qs,self.z),
            (self.x+self.qs,self.y+self.qs,self.z),
            (self.x-self.qs,self.y+self.qs,self.z)
        )
        self.check_traits()

    def check_traits(self):
        for i in range(len(self.traits)):
            if self.traits[i].color==[0,0,0]:
                self.traits.pop(i)

    def __call__(self, *args, **kwargs):
        glPushMatrix()
        glBegin(GL_QUADS)
        glColor3ub(*self.color)
        for vertex in self.matrix:
            glVertex3dv(vertex)
        glEnd()
        self.check_traits()
        for trait in self.traits:
            trait.move()
            trait()
        glPopMatrix()



def draw(*args,**kwargs):
    if "nodes" in kwargs.keys():
        for node in kwargs.get("nodes"):
            node()
            node.move()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

if __name__ == "__main__":
    window()
    fps=pygame.time.Clock()
    nodes=[]
    for _ in range(NODE_SPAWN):
        r=ri(5,255)
        g=ri(5,255)
        b=ri(5,255)
        if r>g and r>b:
            if r<200:
                r=200
            if r - g>50:
                g-=50
            if r - b>50:
                b-=50

        elif g>r and g>b:
            if g < 200:
                g = 200
            if g - r > 50:
                r -= 50
            if g - b > 50:
                b -= 50

        elif b>g and b>r:
            if b < 200:
                b = 200
            if b - r > 50:
                r -= 50
            if b - g > 50:
                g -= 50

        color=(r,g,b)

        nodes.append(Node(ri(50,100),ri(-15,15),ri(500,1000)/100000,ri(0,int(pi*1000)*2)/1000,ri(50,100)/100,color))
    while True:
        fps.tick(60)
        events()
        draw(nodes=nodes)