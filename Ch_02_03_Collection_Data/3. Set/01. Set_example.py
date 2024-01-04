# Set example
se = {'a','a','b'}
# print(se)
# print(sorted(se))
vowels = set('aeiou')
word = "hello"
print(vowels)

# union
union = vowels.union(set(word))
print(union)

# difference
difference = vowels.difference(set(word))
print(difference)

# intersection Reports on Commonality
intersection = vowels.intersection(set(word))
print(intersection)