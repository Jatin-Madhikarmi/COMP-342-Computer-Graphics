from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

data_points = [(50, 60), (100, 120), (150, 90), (200, 160), (250, 130)]

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2i(int(round(x)), int(round(y)))
        x += x_inc
        y += y_inc
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    for i in range(len(data_points) - 1):
        x1, y1 = data_points[i]
        x2, y2 = data_points[i + 1]
        dda_line(x1, y1, x2, y2)

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 300, 0, 200)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 400)
glutCreateWindow(b"Line Graph using DDA Algorithm")
init()
glutDisplayFunc(display)
glutMainLoop()