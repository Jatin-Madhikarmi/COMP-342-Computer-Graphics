from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glColor3f(1.0, 0.0, 0.0)   # Red
    glVertex2f(-0.5, -0.5)

    glColor3f(0.0, 1.0, 0.0)   # Green
    glVertex2f(0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)   # Blue
    glVertex2f(0.0, 0.5)

    glColor3f(0.0,0.0,1.0)
    glVertex2f(0.0,1.0)

    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Polygon Letter J")
 

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

main()
