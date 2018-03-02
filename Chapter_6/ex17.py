
import sys

def test(did_pass):

    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_multiple(f, n):
    if f%n == 0:
        return True
    return False

'''Another Way

def is_multiple(f, n):
    return is_factor(n,f)

def is_factor(f, n):
    if n%f == 0:
        return True
    return False

'''

def test_suit():
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

test_suit()