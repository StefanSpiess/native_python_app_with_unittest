from types import UnionType
def calculate_average(*integers: float) -> float:
    sum = 0

    for integer in integers:
        if type(integer) in [int,float]:
            sum += integer
        else:
            raise TypeError("Input must be integer or float.")

    average = sum / len(integers)

    return average