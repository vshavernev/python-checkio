def TestCell(land_map, row, col):
    result = 0
    if land_map[row][col] == 0:
        land_map[row][col] = -1
    elif land_map[row][col] == 1:
        land_map[row][col] = -1
        result = 1
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    if (row + i >= 0) and (col + j >= 0):
                        if land_map[row + i][col + j] == 1:
                            result += TestCell(land_map, row + i, col + j)
                        elif land_map[row + i][col + j] == 0:
                            land_map[row + i][col + j] = -1
                except IndexError:
                    continue
    
    return result
                

def checkio(land_map):
    islands = []
    for i in range(len(land_map)):
        for j in range(len(land_map[i])):
            island_area = TestCell(land_map, i, j)
            if island_area > 0:
                islands.append(island_area)

    return sorted(islands)
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"

