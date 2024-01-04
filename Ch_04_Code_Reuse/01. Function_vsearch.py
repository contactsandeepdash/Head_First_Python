"""
    triple quotes around strings are known as docstrings
    1. function
    2. collection of functions and package them as a file
    3. collection of files make a module

    the single quote character we use to surround our strings

"""
def search4vowels():
    """ Display any vowles found in an asked-for word   """
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()

