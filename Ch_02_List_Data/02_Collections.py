import collections

how_many = "How many f's are in this string? fffff nnn hhhHH ss"
c = collections.Counter(how_many)
print(c["H"])