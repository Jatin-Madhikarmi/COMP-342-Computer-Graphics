from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Clipping window boundaries
x_min, y_min = -0.5, -0.5
x_max, y_max = 0.5, 0.5

def liang_barsky_clip(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    # p[k] and q[k] values for Left, Right, Bottom, Top
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    
    t1 = 0.0
    t2 = 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Parallel and outside
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > t1: t1 = t
            else:
                if t < t2: t2 = t

    if t1 < t2:
        nx1 = x1 + t1 * dx
        ny1 = y1 + t1 * dy
        nx2 = x1 + t2 * dx
        ny2 = y1 + t2 * dy
        return [(nx1, ny1), (nx2, ny2)]
    
    return None

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw Clipping Window (White)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min); glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max); glVertex2f(x_min, y_max)
    glEnd()

    # Original line coordinates
    p1, p2 = (-0.9, -0.4), (0.8, 0.6)

    # Draw original line (Red - faint/rejected part)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(*p1); glVertex2f(*p2)
    glEnd()

    # Apply clipping
    clipped_line = liang_barsky_clip(p1[0], p1[1], p2[0], p2[1])

    # Draw clipped line (Cyan for Liang-Barsky)
    if clipped_line:
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(*clipped_line[0]); glVertex2f(*clipped_line[1])
        glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Liang-Barsky Line Clipping")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()