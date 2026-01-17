from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Clipping window boundaries
x_max, y_max = 0.5, 0.5
x_min, y_min = -0.5, -0.5

def compute_code(x, y):
    code = INSIDE
    if x < x_min: code |= LEFT
    elif x > x_max: code |= RIGHT
    if y < y_min: code |= BOTTOM
    elif y > y_max: code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            # Line needs clipping
            x, y = 0.0, 0.0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return [(x1, y1), (x2, y2)]
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
    p1, p2 = (-0.8, -0.2), (0.7, 0.9)

    # Draw original line (Red - faint)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(*p1); glVertex2f(*p2)
    glEnd()

    # Apply clipping
    clipped_line = cohen_sutherland_clip(p1[0], p1[1], p2[0], p2[1])

    # Draw clipped line (Green)
    if clipped_line:
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(*clipped_line[0]); glVertex2f(*clipped_line[1])
        glEnd()

    glFlush()

def main():
    glutInit()
    glutCreateWindow(b"Cohen-Sutherland Clipping")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()