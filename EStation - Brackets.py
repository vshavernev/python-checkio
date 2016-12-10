def checkio(expression):
    Stack = list()
    is_balanced = True
    
    for c in expression:
        if c == "{" or c == "(" or c == "[":
            Stack.append(c)
        elif c == "}" or c == ")" or c == "]":
            try:
                cb = Stack.pop()
                is_balanced = (c == "}" and cb == "{") or (c == ")" and cb == "(") or (c == "]" and cb == "[")
            except IndexError as ex:
                is_balanced = False
            finally:
                if not is_balanced:
                    break

    return is_balanced and len(Stack) == 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

