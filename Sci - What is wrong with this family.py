def is_family(tree):
    is_correct = True
    family = []
    is_first_pair = True
    for pair in tree:
        if is_first_pair:
            x, y = map(str, pair)
            family.append(x)
            family.append(y)
            is_first_pair = False
            continue
        x, y = map(str, pair)
        is_correct = (x in family) and (y not in family)
        if is_correct:
            family.append(y)
        else:
            break

    return is_correct


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")

