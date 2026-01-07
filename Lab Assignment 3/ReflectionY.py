from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(50, 50)
    glVertex2f(150, 50)
    glVertex2f(100, 150)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Original Object (White)
    glColor3f(1.0, 1.0, 1.0)
    draw_triangle()

    # Reflection about Y-axis using Homogeneous Matrix logic
    # Matrix: [-1 0 0 | 0 1 0 | 0 0 1]
    glPushMatrix()
    glColor3f(0.0, 1.0, 0.0) # Green
    glScalef(-1.0, 1.0, 1.0) 
    draw_triangle()
    glPopMatrix()
    
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Reflection about Y-Axis")
gluOrtho2D(-250, 250, -250, 250)
glutDisplayFunc(display)
glutMainLoop()