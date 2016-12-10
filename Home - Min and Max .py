def min2(arg1, arg2, key):
    if (key is not None and key(arg1) < key(arg2)) or (key is None and arg1 < arg2):
        return arg1
    else:
        return arg2


def max2(arg1, arg2, key):
    if (key is not None and key(arg2) > key(arg1)) or (key is None and arg2 > arg1):
        return arg2
    else:
        return arg1


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(args[0])

    result = args[0]
    for i in range(1, len(args)):
        result = min2(result, args[i], key)
    
    return result


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(args[0])

    result = args[0]
    for i in range(1, len(args)):
        result = max2(result, args[i], key)
    
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

