# List - an ordered MUTABLE list of homogenous / heterogeneos objects
# Always enclosed in square brackets, and the objects in the list are separated by a comma.
# starts with index = 0

vowels = ['a', 'e', 'i', 'o', 'u']
print("length of vowels = " + str(len(vowels)))
word = "Milliways"
for letter in word:
    if letter in vowels:
        print("vowel = " + letter)
    elif letter not in vowels:
        print("not vowel = " + letter)


#----------------------------------------------------------------------------------------
    # 1. append(the value)
    # 2. remove(not index value; rather the exact value to remove)
    # 3. pop(This is an index value. Zero corresponds to the first object in the list)
    # 4. extend - takes a list of objects as its sole argument
        # example: nums.extend([3, 4])
    # 5. insert: takes an index value and an object as its arguments
        # example: nums.insert(0, 1)

    # List methods change the state of a list, whereas using square brackets and slices (typically) does not.
#----------------------------------------------------------------------------------------
    
