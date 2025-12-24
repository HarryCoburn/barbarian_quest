import random

WEALTH_RESULT = {
    2: [0,1,2,2,3,4]
}


def wealth_check(code):
    roll = random.randint(1,6) - 1
    return WEALTH_RESULT[code][roll]
