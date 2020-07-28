import math

def mirror_numbers(n, factor, mid):
    # https://stackoverflow.com/questions/38130895/find-middle-of-a-list/38131003
    middle = math.floor(float(n) / 2)
    if n % 2 != 0:
        fudge_array_minus = []
        fudge_array_plus = []
        if middle < 1:
            adj = 1
        else:
            adj = 2
        for i in range(1, middle + 1):
            fudge_array_minus.append(-i * adj * factor + mid)
            fudge_array_plus.append(i * adj * factor + mid)
        x = fudge_array_minus[::-1] + [0.0 + mid] + fudge_array_plus
        # x = [-factor * i + mid for i in reversed(range(1, middle + 1))] + [0.0 + mid] + [factor * i + mid for i in range(1, middle + 1)]
        return x
    else:
        acc = 0
        fudge_array_minus = []
        fudge_array_plus = []
        for i in range(1, middle + 1):
            fudge_array_minus.append((-i - acc) * factor + mid)
            fudge_array_plus.append((i + acc) * factor + mid)
            acc += 1
        x = fudge_array_minus[::-1] + fudge_array_plus
        # x = [-factor * i + mid for i in reversed(range(1, middle + 1))] + [factor * i + mid for i in range(1, middle + 1)]
        return x
