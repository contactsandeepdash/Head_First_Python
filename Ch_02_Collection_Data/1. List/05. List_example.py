# List index example

saying = "Don't panic!"
letters = list(saying)
print(len(letters))
print(letters)

#   0   1   2   3   4   5   6   7   8   9   10  11
#   D   O   N   '   T       P   A   N   I   C   !

first = letters[0]
print(first)
print(letters[0])
print(letters[3])
print(letters[6])

print("--------------")

last = letters[-1]
print(last)
print(letters[-1])
print(letters[-3])
print(letters[-6])

print("**************")
# When start is missing, it has a default value of 0.
# When stop is missing, it takes on the maximum value allowable for the list.
# When step is missing, it has a default value of 1.

for l in letters [0: (len(letters)): 2]:
    print(l)
print("^^^^^^^^^^^^^^")
print (letters[0: (len(letters)): 2])

print("^^^^^^^^^^^^^^")
print(letters[::3])

print("^^^^^^^^^^^^^^")
print(letters[0:10:3])

book = "The Hitchhiker's Guide to the Galaxy"
bookList = list(book)
print(bookList)

backwards = bookList[::-1]
print(''.join(backwards))

everyOther = bookList[::-2]
print(''.join(everyOther))
print(''.join(bookList[4:14]))
print(''.join(bookList[13:3:-1]))