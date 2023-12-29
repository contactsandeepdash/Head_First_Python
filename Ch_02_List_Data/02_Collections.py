import collections

how_many = "How many f's are in this string? fffff nnn hhhHH ss"
c = collections.Counter(how_many)
print("Total count of H = " + str(c["H"]))

# List - an ordered MUTABLE list of homogenous / heterogeneos objects
# Always enclosed in square brackets, and the objects in the list are separated by a comma.
# starts with index = 0

vowels = ['a', 'e', 'i', 'o', 'u']
print("length of vowels = " + str(len(vowels)))
word = "Milliways"
for letter in word:
    if letter in vowels:
        print(letter)


# Tuple - an ordered IMMUTABLE list of homogenous / heterogeneos objects - tuple as a constant list


# Dictinoary - an unordered and mutable set of key/value pairs; Each unique key has a value


# Set - an unordered set of unique objects

