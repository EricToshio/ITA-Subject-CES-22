def add_vectors(vector1, vector2):
    sum = []
    for i in range(len(vector1)):
        sum.append(vector1[i] + vector2[i])
    return sum

def scalar_mult(mult, vector):
    result = []
    for value in vector:
        result.append(value*mult)
    return result