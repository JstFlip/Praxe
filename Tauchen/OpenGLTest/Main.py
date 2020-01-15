import pyglet
from pyglet.gl import *

WINDOW_WIDTH        = 800
WINDOW_HEIGHT       = 800
WINDOW_TITLE        = "OpenGL"
WINDOW_RESIZABLE    = True

CS                  = 25

STUPNE              = 5
STUPNE_AUTO         = 2

class Win(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE,resizable=WINDOW_RESIZABLE)
        glEnable(GL_DEPTH_TEST)
        self.vertexs=   [[
                            [-CS,-CS,CS],
                            [CS,-CS,CS],
                            [CS,CS,CS],
                            [-CS,CS,CS]],
                         [
                            [-CS,CS,CS],
                            [CS,CS,CS],
                            [CS,CS,-CS],
                            [-CS,CS,-CS]],
                         [
                            [-CS,CS,-CS],
                            [CS,CS,-CS],
                            [CS,-CS,-CS],
                            [-CS,-CS,-CS]],
                         [
                            [-CS,-CS,-CS],
                            [CS,-CS,-CS],
                            [CS,-CS,CS],
                            [-CS,-CS,CS]],
                         [
                            [-CS,-CS,CS],
                            [-CS,-CS,-CS],
                            [-CS,CS,-CS],
                            [-CS,CS,CS]],
                         [
                            [CS,CS,CS],
                            [CS,-CS,CS],
                            [CS,-CS,-CS],
                            [CS,CS,-CS]
                         ]]
        self.xr=15
        self.yr=0

    def on_draw(self):
        self.clear()
        glPushMatrix()
        glRotatef(self.xr,0,1,0)
        glRotatef(self.yr,1,0,0)
        glBegin(GL_QUADS)
        for face in range(6):
            glColor3ub((15*face+50)%256,(15*face+50)%256,(15*face+50)%256)
            glVertex3d(self.vertexs[face][0][0],self.vertexs[face][0][1],self.vertexs[face][0][2])
            glVertex3d(self.vertexs[face][1][0],self.vertexs[face][1][1],self.vertexs[face][1][2])
            glVertex3d(self.vertexs[face][2][0],self.vertexs[face][2][1],self.vertexs[face][2][2])
            glVertex3d(self.vertexs[face][3][0],self.vertexs[face][3][1],self.vertexs[face][3][2])

        glEnd()
        glPopMatrix()
    def on_resize(self, width, height):
        glViewport(0,0, width,height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(45, width/height, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glTranslatef(0,0,-200)

    def on_text_motion(self, motion):
        if motion==pyglet.window.key.UP:
            self.yr-=STUPNE
        elif motion==pyglet.window.key.RIGHT:
            self.xr += STUPNE
        elif motion==pyglet.window.key.DOWN:
            self.yr += STUPNE
        elif motion==pyglet.window.key.LEFT:
            self.xr -= STUPNE
    def update(self,dt):
        self.xr+=STUPNE_AUTO

window = Win()
pyglet.clock.schedule_interval(window.update,1/60)
pyglet.app.run()