def S(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + S(data[1:])


def checkio(data):
    return S(data)

