# if you need to perform, say, a frequency count, Python’s dictionary works best.

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['i'] = 0
# found['u'] = 0

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) # no need to initialize each variable
        found[letter] += 1

# for k in found:
#     print(k, 'was found', found[k], 'time(s).')

# for k in sorted(found):
#     print(k, 'was found', found[k], 'time(s).')

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')