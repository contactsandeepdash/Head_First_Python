def search4vowels2(word):
    # Display any vowles found in an asked-for word
    vowels = set('aeiou')
    return vowels.intersection(set(word))

print(search4vowels2('sandeep'))

