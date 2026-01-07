from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot_points(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)
    glEnd()

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    
    plot_points(xc, yc, x, y)
    
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_points(xc, yc, x, y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Draw a circle at center (250, 250) with radius 100
    midpoint_circle(250, 250, 100)
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Circle Algorithm")
    gluOrtho2D(0, 500, 0, 500)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()