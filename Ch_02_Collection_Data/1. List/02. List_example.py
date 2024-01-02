# List - an ordered MUTABLE list of homogenous / heterogeneos objects
# Always enclosed in square brackets, and the objects in the list are separated by a comma.
# starts with index = 0

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:    
    print("vowel = " + vowel)


#----------------------------------------------------------------------------------------
    # 1. append(the value)
    # 2. remove(not index value; rather the exact value to remove)
    # 3. pop(This is an index value. Zero corresponds to the first object in the list)
    # 4. extend - takes a list of objects as its sole argument
        # example: nums.extend([3, 4])
    # 5. insert: takes an index value and an object as its arguments
        # example: nums.insert(0, 1)
#----------------------------------------------------------------------------------------
    
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


print("------------------")

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
