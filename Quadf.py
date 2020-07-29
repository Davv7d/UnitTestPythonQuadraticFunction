import math
class Quadratic_function:
    @staticmethod
    def delta(a, b, c):
        if not (isinstance(a, (int, float)) and
                isinstance(b, (int, float)) and
                isinstance(c, (int, float))):
            return None
        delta = b*b - 4*(a*c)
        if delta < 0:
            return None
        return delta

    @staticmethod
    def zero_place(a, b, c):
        delta = Quadratic_function.delta(a, b, c)
        if(delta is None or a == 0):
            # print("delta < 0")
            return None
        elif(delta == 0):
            # print("delta == 0")
            return -b/(2*a)
        pdelta = math.sqrt(delta)
        return ((-b - pdelta)/(2*a)), ((-b + pdelta)/(2*a))

if __name__ == "__main__":
    f1_result = Quadratic_function.miejsca_zerowe(1, 6, 8)
    print(f1_result)