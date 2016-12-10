def safe_pawns(pawns):
    
    position = set()
    for i in pawns:
        icol = "abcdefgh".find(i[0])
        irow = "12345678".find(i[1])
        position.add((icol, irow))

    counter = 0
    for i in position:
        icol = i[0]
        irow = i[1]
        if (icol - 1, irow - 1) in position or (icol + 1, irow - 1) in position:
            counter += 1

    return counter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

