import sys


def test(did_pass):

    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


#a)Return only those items that are present in both lists.
def find_a_merge_pattern(list1, list2):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            return result

        if yi >= len(list2):
            return result

        if list1[xi] == list2[yi]:  # Good, word exists in list1
            result.append(list2[yi])
            yi += 1

        elif list1[xi] < list2[yi]: # Move past this list1 word,
            xi += 1

        else:                     # Got word that is not in list1
            yi += 1

#b)Return only those items that are present in the first list, but not in the second.
def find_b_merge_pattern(list1, list2):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            return result

        if yi >= len(list2):
            result.extend(list1[xi:])
            return result

        if list1[xi] == list2[yi]:  # Good, word exists in list1
            xi += 1

        elif list1[xi] < list2[yi]: # Move past this list1 word,
            result.append(list1[xi])
            xi += 1

        else:                     # Got word that is not in list1
            yi += 1

#c)Return only those items that are present in the second list, but not in the first.
def find_c_merge_pattern(list1, list2):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            result.extend(list2[yi:])
            return result

        if yi >= len(list2):
            return result

        if list1[xi] == list2[yi]:  # Good, word exists in list1
            yi += 1

        elif list1[xi] < list2[yi]: # Move past this list1 word,
            xi += 1

        else:                     # Got word that is not in list1
            result.append(list2[yi])
            yi += 1


#d)Return items that are present in either the first or the second list.
def find_d_merge_pattern(list1, list2):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            result.extend(list2[yi:])
            return result

        if yi >= len(list2):
            result.extend(list1[xi:])
            return result

        if list1[xi] == list2[yi]:  # Good, word exists in list1
            result.append(list1[xi])
            yi += 1

        elif list1[xi] < list2[yi]: # Move past this list1 word,
            result.append(list1[xi])
            xi += 1

        else:                     # Got word that is not in list1
            result.append(list2[yi])
            yi += 1

#e)Return items from the first list that are not eliminated by a matching element in the second list. In this case, an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
def find_e_merge_pattern(list1, list2):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            return result

        if yi >= len(list2):
            result.extend(list1[xi:])
            return result

        if list1[xi] == list2[yi]:  # Good, word exists in list1
            yi += 1
            xi += 1

        elif list1[xi] < list2[yi]: # Move past this list1 word,
            result.append(list1[xi])
            xi += 1

        else:                     # Got word that is not in list1
            yi += 1


a = [5, 7, 11, 11, 11, 12, 13]
b = [7, 8, 11]


test (find_a_merge_pattern(a, b) == [7, 11])
test (find_b_merge_pattern(a, b) == [5, 12, 13])
test (find_c_merge_pattern(a, b) == [8])
test (find_d_merge_pattern(a, b) == [5, 7, 7, 8, 11, 11, 11, 11, 12, 13])
test (find_e_merge_pattern(a, b) == [5,11,11,12,13])
