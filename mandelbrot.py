"""
 Simple drawing of Mandlebrot
 by Ojas

 Based on https://www.bowdoin.edu/~dfrancis/askanerd/mandelbrot/
 and processing examples, Mandlebrot

 TODO:
 - is there some magic we can add with Euler?
    0 = e^2pi*i - 1
"""

import pygame
import cmath
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_size = (400, 300)

def get_c1(c, max_iterations):
    a = c[0]
    b = c[1]
    n = 0
    while n < max_iterations:
        aa = a * a
        bb = b * b
        twoab = 2.0 * a * b
        a = aa - bb + c[0]
        b = twoab + c[1]
        # Infinty in our finite world is simple, let's just consider it 16
        # if (aa**aa + bb*bb)**(1/2.0) > 4.0:
        if abs(aa**aa + bb*bb) > 16.0:
            return n
            # break
        n += 1

def get_c2(c, max_iterations):
    """
        Z = Z² + C

        where Z is in the form a+bi
        Z = (a+bi) * (a+bi) + C
        Z = a*a + 2*a*bi + bi * bi
        Z = a*a + 2*a*bi - b*b
        Z = a*a-b*b + 2abi
    """
    n = 0

    # initially z is 0, so we can simplyify
    a, b = c
    while n<max_iterations:
        aa = a*a
        bb = b*b
        a, b = aa - bb + c[0], 2.0 * a * b + c[1]
        if abs(aa + bb) > 16.0:
            return n
        n += 1

def get_c3(c, max_iterations):
    c_ = complex(*c)
    n = 0
    z = 0
    while n<max_iterations:
        z = z*z + c_
        if cmath.polar(z)[0] > 4.0:
            return n
        n += 1

def draw():
    w = 4
    h = w * screen_size[1] / screen_size[0]
    mins = (-w/2, -h/2)
    maxs = (mins[0] + w, mins[1] + h)
    dx = w / screen_size[0]
    dy = h / screen_size[1]
    max_iterations = 100

    x = mins[0]

    pixel_arr = pygame.PixelArray(screen)
    compute_time = 0

    for screen_x in range(screen_size[0]):
        y = mins[1]
        for screen_y in range(screen_size[1]):
            t1 = time.time ()

            # n = get_c1((x, y), max_iterations)
            n = get_c2((x, y), max_iterations)
            # n = get_c3((x, y), max_iterations)

            t2 = time.time ()
            compute_time += t2-t1
            if n is not None:
                cc = 255.0 * n / max_iterations
                color = (cc, cc, cc)
                pixel_arr[screen_x, screen_y] = color
            y += dy
        x += dx
    print(compute_time)
#    pygame.surfarray.blit_array(screen, pixels)


pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Mandlebrot")

# Loop until the user clicks the close button.
done = False
s = 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    if s == 0:
        screen.fill(BLACK)
        draw()
        s = 1

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
