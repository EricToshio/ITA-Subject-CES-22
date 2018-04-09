import time
def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main(size, printable):
    total_time = 0
    initial_time = time.time()
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(size))     # Generate the initial permutation
    found = False
    tries = 0
    while not found:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           final_time = time.time()
           total_time = final_time - initial_time
           if printable:
               print("Found solution {0} for a board of size {1} in {2} tries in {3:.2f} seconds".format(bd, size, tries, total_time))
           tries = 0
           found = True
    return total_time


def can_be_usually_solved_under_minute(tries_to_be_usually_accepted):
    i = 4
    total_time = 0
    while total_time < tries_to_be_usually_accepted*60:
        print("test board of size :", i)
        total_time = 0
        for _ in range(tries_to_be_usually_accepted):
            total_time += main(i, False)
        i += 2
    return i


#find solution for a board of size 4
main(4, True)
#find soltuion for a board of size 12
main(12, True)
#find soltuion for a board of size 16
main(16, True)

#get a solution under a minute max size puzzle
size = can_be_usually_solved_under_minute(5) - 2

#Usually the result is size == 16
print("the maximum size puzzle you can usually solve in under a minute is {0}".format(size))
