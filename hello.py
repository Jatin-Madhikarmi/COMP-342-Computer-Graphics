from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)   # Red
    glVertex2f(-0.5, -0.5)

    glColor3f(0.0, 1.0, 0.0)   # Green
    glVertex2f(0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)   # Blue
    glVertex2f(0.0, 0.5)
    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"PyOpenGL Triangle")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)

    glutMainLoop()

if __name__ == "__main__":
    main()
