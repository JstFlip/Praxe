from OpenGL.GL import glEnable, GL_DEPTH_TEST, GL_BLEND, glViewport, glMatrixMode, GL_PROJECTION, glLoadIdentity, GL_MODELVIEW, glTranslatef
from OpenGL.GLU import gluPerspective
from pygame import event, QUIT
from pygame import init, DOUBLEBUF, OPENGL, GL_MULTISAMPLEBUFFERS, GL_MULTISAMPLESAMPLES, FULLSCREEN
from pygame import quit as pquit
from pygame.display import set_mode, gl_set_attribute
from var import *


def setup_window():
    init()
    set_mode(WINDOW_SIZE, DOUBLEBUF | OPENGL | FULLSCREEN)
    if WINDOW_MSAA:
        gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
        gl_set_attribute(GL_MULTISAMPLESAMPLES, WINDOW_MSAA)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)


def setup_opengl():
    glViewport(0, 0, 1920,1080)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, 1600 / 900, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -800)


def window():
    setup_window()
    setup_opengl()


def event_hendler():
    for events in event.get():
        if events.type == QUIT or events.__dict__.get("key") == 27:
            pquit()
            quit()
