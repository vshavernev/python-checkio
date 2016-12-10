def checkio(words):
    
    counter = 0
    for s in words.split():
        counter = 0 if s.isdigit() else counter + 1
        if counter == 3:
            break

    return counter == 3


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"


