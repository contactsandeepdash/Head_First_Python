import collections

how_many = "How many f's are in this string? fffff nnn hhhHH ss"
c = collections.Counter(how_many)
print("Total count of H = " + str(c["H"]))




# Tuple - an ordered IMMUTABLE list of homogenous / heterogeneos objects - tuple as a constant list


# Dictinoary - an unordered and mutable set of key/value pairs; Each unique key has a value


# Set - an unordered set of unique objects

l = list()
print(l)
l = [ 1, 2, 3 ]
print(l)

d = dict()
print(d)
d = { 'first': 1, 'second': 2, 'third': 3 }
print(d)

s = set()
print(s)
s = {1, 2, 3}
print(s)

t = tuple()
print(t)
t = (1, 2, 3)
print(t)

