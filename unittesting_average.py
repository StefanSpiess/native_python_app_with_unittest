from types import UnionType
def average_of_integers(*integers):
    sum = 0

    for integer in integers:
        if type(integer) in [int,float]:
            sum += integer
        else:
            raise TypeError("Input must be integer or float.")

    average = sum / len(integers)

    return average