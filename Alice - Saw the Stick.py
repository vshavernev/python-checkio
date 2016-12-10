def checkio(number):
    triangle_numbers = []

    i = 1
    inc = 2
    while i < 1000:
        triangle_numbers.append(i)
        i += inc
        inc += 1

    result = []
    is_solved = False
    for i in range(len(triangle_numbers)):
        result = []
        sum_of_triangles = 0
        for j in triangle_numbers[i:]:
            result.append(j)
            sum_of_triangles += j
            if sum_of_triangles == number:
                is_solved = True
                break
            elif sum_of_triangles > number:
                break
        if is_solved:
            break

    if not is_solved:
        result = []

    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"

