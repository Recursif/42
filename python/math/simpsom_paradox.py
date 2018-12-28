

def get_ration(victory, defeat):
    total = victory + defeat
    return (victory/ total)

def get_inverse_ratio(ratio):
    if (ratio == 0):
        return 1
    elif (ratio == 1):
        return 0
    elif (ratio > 0 and ratio < 1):
        return 1/ratio
    else:
        return -1

def get_ratio_v1_v2(t, t1, t2):
    numerator = t * t1 - t * t1 * t2 - t2
    divisor = t1 * t2 - t * t2 - t1 

    return numerator / divisor 




