def find_message(text):
    result = ""
    for c in text:
        if c.isupper():
            result += c
            
    return result

# Другой вариант
# find_message = lambda text: ''.join(filter(str.isupper, text))
#

# Другой вариант
# def find_message(text):
#     return ''.join(c for c in text if c.isupper())
#
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

