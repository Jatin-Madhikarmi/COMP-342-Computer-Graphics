from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xc, yc = 0, 0
a, b = 120, 80

def plot(x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)

def midpoint_ellipse():
    x = 0
    y = b

    p1 = b*b - a*a*b + 0.25*a*a

    glBegin(GL_POINTS)
    while (2*b*b*x) <= (2*a*a*y):
        plot(x, y)
        if p1 < 0:
            x += 1
            p1 += 2*b*b*x + b*b
        else:
            x += 1
            y -= 1
            p1 += 2*b*b*x - 2*a*a*y + b*b

    p2 = b*b*(x + 0.5)**2 + a*a*(y - 1)**2 - a*a*b*b

    while y >= 0:
        plot(x, y)
        if p2 > 0:
            y -= 1
            p2 += a*a - 2*a*a*y
        else:
            x += 1
            y -= 1
            p2 += 2*b*b*x - 2*a*a*y + a*a
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    midpoint_ellipse()

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-200, 200, -200, 200)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Midpoint Ellipse Drawing Algorithm")
init()
glutDisplayFunc(display)
glutMainLoop()