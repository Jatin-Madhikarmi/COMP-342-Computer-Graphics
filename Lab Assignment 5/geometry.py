from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_axes():
    """Draws X (Red), Y (Green), and Z (Blue) axes for reference."""
    glBegin(GL_LINES)
    # X axis
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(1.0, 0.0, 0.0)
    # Y axis
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 1.0, 0.0)
    # Z axis
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 0.0, 1.0)
    glEnd()

def draw_teapot(color):
    """Renders a wireframe teapot."""
    glColor3f(*color)
    glutWireTeapot(0.5)