class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

def is_colliding(rec1, rec2):
    """

    :param rec1: rectangle1 (where corner is the left - down corner)
    :param rec2: rectangle2 (where corner is the left - down corner)
    :return: if they are colliding
    """
    collide_x = False
    collide_y = False
    difx = rec1.corner.x - rec2.corner.x
    dify = rec1.corner.y - rec2.corner.y
    if(difx >= 0 and rec1.corner.x <= (rec2.corner.x + rec2.width)):
        collide_x = True
    elif(difx <= 0 and rec2.corner.x <= (rec1.corner.x + rec1.width)):
        collide_x = True

    if (dify >= 0 and rec1.corner.y <= (rec2.corner.y + rec2.height)):
        collide_y = True
    elif (dify <= 0 and rec2.corner.y <= (rec1.corner.y + rec1.height)):
        collide_y = True

    return collide_x and collide_y


assert (is_colliding(Rectangle(Point(0, 0), 10, 5), Rectangle(Point(2, 4), 5, 6)))