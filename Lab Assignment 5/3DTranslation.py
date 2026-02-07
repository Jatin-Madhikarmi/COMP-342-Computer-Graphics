from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Move the camera back so we can see both shapes
    glTranslatef(0.0, 0.0, -7.0)

    # --- Teapot 1: At the Origin (0, 0, 0) ---
    glPushMatrix()
    glColor3f(0.0, 0.8, 1.0) # Cyan
    glutWireTeapot(0.5)
    glPopMatrix()

    # --- Teapot 2: Translated (Moved 2 units on X-axis) ---
    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0) # Move 2.0 units to the right
    glColor3f(1.0, 0.0, 0.0)    # Red
    glutWireTeapot(0.5)
    glPopMatrix()

    glutSwapBuffers()

# GLUT Setup
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Original vs Translated Teapot")

init()
glutDisplayFunc(draw)
glutReshapeFunc(reshape)
glutMainLoop()