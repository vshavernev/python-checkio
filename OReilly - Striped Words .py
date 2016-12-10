import re

def checkio(text):
    vowels = "AEIOUY"
    consonants = "BCDFGHJKLMNPQRSTVWXZ"

    list_of_words = re.findall(r"[\w']+", text)
    counter = 0

    for word in list_of_words:
        is_striped_word = False
        position = 0
        for c in word.upper():
            if not (c in vowels or c in consonants):
                is_striped_word = False
                break
            if position == 0:
                first_letter_is_vowel = (c in vowels)
            else:
                if first_letter_is_vowel:
                    if c in consonants:
                        is_striped_word = (position % 2 == 1)
                    else:
                        is_striped_word = (position % 2 == 0)
                else:
                    if c in consonants:
                        is_striped_word = (position % 2 == 0)
                    else:
                        is_striped_word = (position % 2 == 1)
                if not is_striped_word:
                    break
            position += 1
    
        if is_striped_word:
            counter += 1

    return counter


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

