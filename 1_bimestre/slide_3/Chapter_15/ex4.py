import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def get_line_to(self, point):
        a = (self.y - point.y)/(self.x - point.x)
        b = self.y - a*self.x
        return (a, b)


test(Point(4, 11).get_line_to(Point(6, 15)) == (2, 3))

#this function will fail when point.x == self.x
"""
print(Point(5,13).slope_from_origin(5,74))
"""