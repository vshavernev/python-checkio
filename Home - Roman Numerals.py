def checkio(data):

    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hund = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thos = ['', 'M', 'MM', 'MMM']

    n3 = data // 1000
    n2 = (data - (1000 * n3)) // 100
    n1 = (data - (1000 * n3) - (100 * n2)) // 10
    n0 = data - (1000 * n3) - (100 * n2) - (10 * n1)

    return thos[n3] + hund[n2] + tens[n1] + ones[n0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

    checkio(int(input()))
