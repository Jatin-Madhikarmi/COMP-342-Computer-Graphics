from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def round_val(v):
    return int(v + 0.5)

def draw_dda():
    # Endpoints of the line
    x1, y1 = 50, 50
    x2, y2 = 450, 300

    dx = x2 - x1
    dy = y2 - y1

    # Find the number of steps
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate increments
    x_inc = dx / float(steps)
    y_inc = dy / float(steps)

    # Starting coordinates
    x, y = x1, y1

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 1.0)  # Cyan color
    glBegin(GL_POINTS)

    for _ in range(int(steps) + 1):
        glVertex2i(round_val(x), round_val(y))
        x += x_inc
        y += y_inc

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"DDA Line Drawing Algorithm")
    
    # Initialize projection
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 500, 0, 500)
    
    glutDisplayFunc(draw_dda)
    glutMainLoop()

if __name__ == "__main__":
    main()