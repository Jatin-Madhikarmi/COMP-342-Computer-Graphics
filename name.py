from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_jatin():
    # Set color to a bright Green (RGB: 0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)

    # --- Letter J ---
    glBegin(GL_POLYGON)
    glVertex2f(10, 80); glVertex2f(40, 80); glVertex2f(40, 70); glVertex2f(10, 70)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20, 70); glVertex2f(30, 70); glVertex2f(30, 20); glVertex2f(20, 20)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(10, 30); glVertex2f(20, 30); glVertex2f(20, 20); glVertex2f(10, 20)
    glEnd()

    # --- Letter A ---
    glBegin(GL_POLYGON)
    glVertex2f(50, 20); glVertex2f(60, 80); glVertex2f(65, 80); glVertex2f(55, 20)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(80, 20); glVertex2f(70, 80); glVertex2f(65, 80); glVertex2f(75, 20)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(55, 45); glVertex2f(75, 45); glVertex2f(75, 40); glVertex2f(55, 40)
    glEnd()

    # --- Letter T ---
    glBegin(GL_POLYGON)
    glVertex2f(90, 80); glVertex2f(120, 80); glVertex2f(120, 70); glVertex2f(90, 70)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(100, 70); glVertex2f(110, 70); glVertex2f(110, 20); glVertex2f(100, 20)
    glEnd()

    # --- Letter I ---
    glBegin(GL_POLYGON)
    glVertex2f(130, 80); glVertex2f(140, 80); glVertex2f(140, 20); glVertex2f(130, 20)
    glEnd()

    # --- Letter N ---
    glBegin(GL_POLYGON)
    glVertex2f(150, 20); glVertex2f(160, 20); glVertex2f(160, 80); glVertex2f(150, 80)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(150, 80); glVertex2f(160, 80); glVertex2f(180, 20); glVertex2f(170, 20)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(170, 20); glVertex2f(180, 20); glVertex2f(180, 80); glVertex2f(170, 80)
    glEnd()

def display():
    # Clear the screen and the depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Move the drawing slightly so it's centered
    draw_jatin()
    
    # Swap buffers for a smooth render
    glutSwapBuffers()

def reshape(w, h):
    """Handle window resizing so the coordinate system stays consistent."""
    if h == 0: h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # This defines the "drawing paper" coordinates (0-200 width, 0-100 height)
    gluOrtho2D(0, 200, 0, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    # Use GLUT_DOUBLE for better compatibility
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 400)
    glutCreateWindow(b"JATIN - OpenGL")
    
    glClearColor(0.0, 0.0, 0.0, 1.0) # Black background
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape) # Important for coordinate mapping
    
    glutMainLoop()

if __name__ == "__main__":
    main()


    