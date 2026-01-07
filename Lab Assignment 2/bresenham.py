from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_bresenham_line(x0, y0, x1, y1):
    """Generalized Bresenham Line Drawing Algorithm"""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    glBegin(GL_POINTS)
    while True:
        glVertex2i(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) 
    # Example Lines
    draw_bresenham_line(50, 50, 400, 200) # |m| < 1
    draw_bresenham_line(50, 50, 200, 400) # |m| > 1
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 500, 0, 500)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Bresenham Line Algorithm")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()