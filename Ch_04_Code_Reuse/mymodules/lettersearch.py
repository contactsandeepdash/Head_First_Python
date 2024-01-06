"""
    We are stating that the phrase argument is expected to be a string.
    And the function returns a set to its caller.
"""

def search4vowels(phrase:str) -> set:
    """ Display any vowles found in an asked-for phrase     """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ return a set of the 'letters' found in the 'phrase'  """
    return set(letters).intersection(set(phrase))

