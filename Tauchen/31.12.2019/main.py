import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from random import randint as ri
from math import sqrt

WINDOW_SIZE = (1920,1080)
MSAA        = 320

ROTATION_SPEED = 0.5
ROTATION = 0
ROTATION_METRIX = (1,3,0)

QUAD_SIZE   = 0.5
QUAD_SPAWN  = 100
QUAD_LINES  = 3
QUAD_SPEED_MULTIPLAYER = 0.5

BOUNDS = (120,120,120)
DRAW_BOUNDS = False

OUTSIDE = False

#################### Window Setup + OpenGL ####################################

def window():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_mode(WINDOW_SIZE,pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN)
    if MSAA:
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS,1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES,MSAA)

    glViewport(0,0, WINDOW_SIZE[0],WINDOW_SIZE[1])
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70,WINDOW_SIZE[0]/WINDOW_SIZE[1],0.1,1000)
    if OUTSIDE:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0,0,-250)

def event_handler(*args):
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.__dict__.get("key")==27:
            pygame.quit()
            quit()
        if event.type==2 and event.__dict__.get("key")==pygame.K_r:
            reset_quads(args[0])

##############################################################################

#############################Drawing And Node Class###########################

class Node:
    def __init__(self,x,y,z,smer,rotation):
        self.x=x
        self.y=y
        self.z=z
        self.smer=smer
        self.size=QUAD_SIZE
        self.rotation=rotation
        self.matrix=((-self.size,-self.size,self.size),(self.size,-self.size,self.size),(self.size,self.size,self.size),(-self.size,self.size,self.size))

    def update(self):
        self.rotation-=ROTATION_SPEED
        self.matrix=((-self.size,-self.size,self.size),(self.size,-self.size,self.size),(self.size,self.size,self.size),(-self.size,self.size,self.size))

    def move(self):
        self.x+=self.smer[0]
        self.y+=self.smer[1]
        self.z+=self.smer[2]
        self.update()

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x,self.y,self.z)
        if ROTATION_METRIX[0]+ROTATION_METRIX[1]+ROTATION_METRIX[2]:
            glRotatef(self.rotation, ROTATION_METRIX[0], ROTATION_METRIX[1], ROTATION_METRIX[2])
        glBegin(GL_QUADS)

        for vertex in self.matrix:
            glVertex3dv(vertex)

        glEnd()
        glPopMatrix()

def draw_objects(*args,):
    for arg in args:
        arg()

def draw_bounds():
    s=BOUNDS
    vertexs=((-s[0],-s[1],s[2]),(s[0],-s[1],s[2]),(s[0],s[1],s[2]),(-s[0],s[1],s[2]),(-s[0],-s[1],-s[2]),(s[0],-s[1],-s[2]),(s[0],s[1],-s[2]),(-s[0],s[1],-s[2]))
    lines=((0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,6),(6,7),(7,4),(7,3),(1,5),(6,2))
    glBegin(GL_LINES)

    for line in lines:
        glVertex3dv(vertexs[line[0]])
        glVertex3dv(vertexs[line[1]])

    glEnd()

def draw_line(a,b):
    glBegin(GL_LINES)
    glVertex3dv(a)
    glVertex3dv(b)
    glEnd()

def draw(quads,lines):
    if ROTATION_METRIX[0] + ROTATION_METRIX[1] + ROTATION_METRIX[2]:
        glRotatef(ROTATION_SPEED,ROTATION_METRIX[0], ROTATION_METRIX[1], ROTATION_METRIX[2])
    @draw_objects
    def draw():
        for quad in quads:
            quad.draw()
        if lines:
            for line in lines:
                draw_line(line[0],line[1])
        if DRAW_BOUNDS:
            draw_bounds()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

##############################################################################

def spawn_quads(quads,rotation=ROTATION):
    for _ in range(QUAD_SPAWN):
        quads.append(Node(0,0,0,[(ri(-100000,100000)/500000)*QUAD_SPEED_MULTIPLAYER,(ri(-100000,100000)/500000)*QUAD_SPEED_MULTIPLAYER,(ri(-100000,100000)/500000)*QUAD_SPEED_MULTIPLAYER],rotation))

def move_quads(quads):
    for quad in quads:
        quad.move()

def reset_quads(quads):
    rotation=quads[0].rotation
    quads.clear()
    spawn_quads(quads,rotation)

def update(x,y,z,quads):
    a = 0
    for i in quads:
        quads_x[a] = i.x
        quads_y[a] = i.y
        quads_z[a] = i.z
        a += 1
    x,y,z = sort(x,y,z)
    check(x,y,z,quads)
    return (x,y,z)


def sort(x,y,z):
    x={k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    y={k: v for k, v in sorted(y.items(), key=lambda item: item[1])}
    z={k: v for k, v in sorted(z.items(), key=lambda item: item[1])}
    return (x,y,z)

def check(xd,yd,zd,quads):
    xv=list(xd.values())
    xk=list(xd.keys())
    x_min=[]
    x_max=[]

    yv = list(yd.values())
    yk = list(yd.keys())
    y_min=[]
    y_max=[]

    zv = list(zd.values())
    zk = list(zd.keys())
    z_min=[]
    z_max=[]

    for x in range(len(xv)):
        if xv[x]<-BOUNDS[0]:
            x_min.append(xk[x])
        else:
            break
    for x in range(len(xv)-1,0,-1):
        if xv[x]>BOUNDS[0]:
            x_max.append(xk[x])
        else:
            break

    for y in range(len(yv)):
        if yv[y] < -BOUNDS[1]:
            y_min.append(yk[y])
        else:
            break
    for y in range(len(yv)-1, 0, -1):
        if yv[y] > BOUNDS[1]:
            y_max.append(yk[y])
        else:
            break

    for z in range(len(zv)):
        if zv[z] < -BOUNDS[2]:
            z_min.append(zk[z])
        else:
            break
    for z in range(len(zv)-1, 0, -1):
        if zv[z] > BOUNDS[2]:
            z_max.append(zk[z])
        else:
            break


    if x_min or x_max:
        for i in x_min+x_max:
            quads[i].smer[0]=-quads[i].smer[0]
            quads[i].move()

    if y_min or y_max:
        for i in y_min+y_max:
            quads[i].smer[1] = -quads[i].smer[1]
            quads[i].move()

    if z_min or z_max:
        for i in z_min+z_max:
            quads[i].smer[2] = -quads[i].smer[2]
            quads[i].move()

def find_index(items,key):
    for i in range(len(items)):
        if items[i][0] == key:
            return i

def find_nearest(x,y,z,xi,yi,zi,oi,quads):
    indexs=[v for v in xi.copy()+yi.copy()+zi.copy() if v!=None]
    o=quads[oi]
    xo=o.x
    yo=o.y
    zo=o.z
    min=float("inf")
    temp=0
    xyz=""
    for i in range(len(indexs)):
        temp=sqrt(pow(quads[indexs[i]].x-xo,2)+pow(quads[indexs[i]].y-yo,2)+pow(quads[indexs[i]].z-zo,2))
        if temp < min:
            min=temp
            index=indexs[i]
            if i==0:
                xyz="X:-"
            elif i==1:
                xyz="X:+"
            elif i==2:
                xyz="Y:-"
            elif i==3:
                xyz="Y:+"
            elif i==4:
                xyz="Z:-"
            elif i==5:
                xyz="Z:+"
    return (index,xyz)




def update_lines(x,y,z,quads):
    xIndexs=[]
    yIndexs=[]
    zIndexs=[]
    xOffset=[-1,1]
    yOffset=[-1,1]
    zOffset=[-1,1]
    xPoint=0
    yPoint=0
    zPoint=0
    lines=[]
    quad=None
    offset=""
    blacklist=[]
    for i in range(len(quads)):
        xOffset = [-1, 1]
        yOffset = [-1, 1]
        zOffset = [-1, 1]
        xPoint = find_index(x, i)
        yPoint = find_index(y, i)
        zPoint = find_index(z, i)
        blacklist.clear()
        for link in range(QUAD_LINES):
            xIndexs.clear()
            yIndexs.clear()
            zIndexs.clear()
            if xPoint+xOffset[0]>=0:
                for _ in range(10):
                    if not x[xPoint+xOffset[0]][0] in blacklist:
                        xIndexs.append(x[xPoint+xOffset[0]][0])
                        break
                    xOffset[0]-=1
                    if xPoint+xOffset[0]<0:
                        xIndexs.append(None)
                        break

            else:
                xIndexs.append(None)
            if xPoint+xOffset[1]<len(quads):
                for _ in range(10):
                    if not x[xPoint+xOffset[1]][0] in blacklist:
                        xIndexs.append(x[xPoint+xOffset[1]][0])
                        break
                    xOffset[1]+=1
                    if xPoint+xOffset[1]>=len(quads):
                        xIndexs.append(None)
                        break
            else:
                xIndexs.append(None)

            if yPoint+yOffset[0]>=0:
                for _ in range(10):
                    if not y[yPoint + yOffset[0]][0] in blacklist:
                        yIndexs.append(y[yPoint + yOffset[0]][0])
                        break
                    yOffset[0] -= 1
                    if yPoint+yOffset[0]<0:
                        yIndexs.append(None)
                        break
            else:
                yIndexs.append(None)
            if yPoint+yOffset[1]<len(quads):
                for _ in range(10):
                    if not y[yPoint + yOffset[1]][0] in blacklist:
                        yIndexs.append(y[yPoint + yOffset[1]][0])
                        break
                    yOffset[1] += 1
                    if yPoint+yOffset[1]>=len(quads):
                        yIndexs.append(None)
                        break
            else:
                yIndexs.append(None)

            if zPoint+zOffset[0]>=0:
                for _ in range(10):
                    if not z[zPoint + zOffset[0]][0] in blacklist:
                        zIndexs.append(z[zPoint + zOffset[0]][0])
                        break
                    zOffset[0] -= 1
                    if zPoint + zOffset[0] < 0:
                        zIndexs.append(None)
                        break
            else:
                zIndexs.append(None)
            if zPoint+zOffset[1]<len(quads):
                for _ in range(10):
                    if not z[zPoint + zOffset[1]][0] in blacklist:
                        zIndexs.append(z[zPoint + zOffset[1]][0])
                        break
                    zOffset[1] += 1
                    if zPoint+zOffset[1]>=len(quads):
                        zIndexs.append(None)
                        break
            else:
                zIndexs.append(None)
            quad, offset=find_nearest(x,y,z,xIndexs,yIndexs,zIndexs,i,quads)
            blacklist.append(quad)
            offset=offset.strip(":")
            if offset[0]=="X":
                if offset[1]=="-":
                    xOffset[0]-=1
                if offset[1]=="+":
                    xOffset[1]+=1
            if offset[0]=="Y":
                if offset[1]=="-":
                    yOffset[0]-=1
                if offset[1]=="+":
                    yOffset[1]+=1
            if offset[0]=="Z":
                if offset[1]=="-":
                    zOffset[0]-=1
                if offset[1]=="+":
                    zOffset[1]+=1
            lines.append(((quads[i].x,quads[i].y,quads[i].z),(quads[quad].x,quads[quad].y,quads[quad].z)))
    return lines


if __name__ == "__main__":
    window()
    fps = pygame.time.Clock()
    events=event_handler
    quads=[]
    spawn_quads(quads)
    quads_x={}
    quads_y={}
    quads_z={}
    lines=[]
    a=0
    for i in quads:
        quads_x[a]=i.x
        quads_y[a]=i.y
        quads_z[a]=i.z
        a+=1

    while True:
        fps.tick(60)
        events(quads)
        move_quads(quads)
        quads_x, quads_y, quads_z = update(quads_x,quads_y,quads_z,quads)
        lines=update_lines(list(quads_x.items()), list(quads_y.items()), list(quads_z.items()), quads)
        draw(quads,lines)