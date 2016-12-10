import math


def get_oblate_spheroid_area(a, c):
    e = math.sqrt(1 - (c**2/a**2))
    return (2 * math.pi * a**2) * (1 + (((1 - e**2)/e) * math.atanh(e)))


def get_prolate_spheroid_area(a, c):
    e = math.sqrt(1 - (a**2/c**2))
    return (2 * math.pi * a**2) * (1 + ((c/(a * e)) * math.asin(e)))


def get_sphere_area(r):
    return 4 * math.pi * r**2


def get_spheroid_volume(a, c):
    return 4/3 * math.pi * a**2 * c


def get_result(x, y):
    return [round(x, 2), round(y, 2)]

def checkio(height, width):
    c = height/2.0
    a = width/2.0
    
    result = []
    if c < a:
        result = get_result(get_spheroid_volume(a, c), get_oblate_spheroid_area(a, c))
    elif c > a:
        result = get_result(get_spheroid_volume(a, c), get_prolate_spheroid_area(a, c))
    else:
        result = get_result(get_spheroid_volume(a, a), get_sphere_area(a))

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"

