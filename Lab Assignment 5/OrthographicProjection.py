from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_cube():
    """Renders a simple wireframe cube."""
    glBegin(GL_LINES)
    # Front Face
    glVertex3f(-1, -1,  1); glVertex3f( 1, -1,  1)
    glVertex3f( 1, -1,  1); glVertex3f( 1,  1,  1)
    glVertex3f( 1,  1,  1); glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1,  1); glVertex3f(-1, -1,  1)
    # Back Face
    glVertex3f(-1, -1, -1); glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1, -1); glVertex3f( 1,  1, -1)
    glVertex3f( 1,  1, -1); glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1, -1); glVertex3f(-1, -1, -1)
    # Connecting Lines
    glVertex3f(-1, -1,  1); glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1,  1); glVertex3f( 1, -1, -1)
    glVertex3f( 1,  1,  1); glVertex3f( 1,  1, -1)
    glVertex3f(-1,  1,  1); glVertex3f(-1,  1, -1)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # --- Orthographic Projection Setup ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # glOrtho(left, right, bottom, top, near, far)
    # This creates a parallel viewing volume.
    glOrtho(-2.0, 2.0, -2.0, 2.0, -5.0, 5.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Rotate the view slightly so we can see the 3D effect
    glRotatef(20, 1, 0, 0)
    glRotatef(20, 0, 1, 0)
    
    glColor3f(1.0, 1.0, 1.0) # White lines
    draw_cube()
    
    glutSwapBuffers()

def main():
    # Initialize GLUT
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Pure PyOpenGL Orthographic Projection")
    
    # Set the display function
    glutDisplayFunc(display)
    
    # Basic Opengl Setup
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    
    # Start the main loop
    glutMainLoop()

if __name__ == "__main__":
    main()