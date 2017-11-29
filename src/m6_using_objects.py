"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Fuyue Li.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    window = rg.RoseWindow()

    center_point1 = rg.Point(200, 150)
    radius1 = 50
    circle1 = rg.Circle(center_point1, radius1)
    circle1.fill_color = 'green'
    circle1.attach_to(window)

    center_point2 = rg.Point(100, 50)
    radius2 = 30
    circle2 = rg.Circle(center_point2, radius2)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow()

    center_point3 = rg.Point(50, 100)
    circle3 = rg.Circle(center_point3, 30)
    circle3.fill_color = 'blue'
    circle3.attach_to(window)

    print(circle3.outline_thickness)
    print(circle3.fill_color)
    print(center_point3)
    print(center_point3.x)
    print(center_point3.y)

    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    center_point4 = rg.Rectangle.get_center(rectangle)
    print(center_point4)
    x = rg.Rectangle.get_center(rectangle).x
    y = rg.Rectangle.get_center(rectangle).y
    print(x)
    print(y)

    window.render()

    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    window = rg.RoseWindow()

    point3 = rg.Point(50, 100)
    point4 = rg.Point(100, 200)
    line1 = rg.Line(point3, point4)
    line1.attach_to(window)

    point5 = rg.Point(25, 50)
    line2 = rg.Line(point3, point5)
    line2.thickness = 10
    line2.attach_to(window)

    center_point5 = rg.Line.get_midpoint(line2)
    print(center_point5)
    x = rg.Line.get_midpoint(line2).x
    y = rg.Line.get_midpoint(line2).y
    print(x)
    print(y)

    window.render()

    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
