# print range(5)
print(range(5))     # range(0, 5)

# print list of range 5
list5 = list(range(0,5))
print(list5)        # [0, 1, 2, 3, 4]

# print 0 to 10 ascending
list10Asc = list(range(0, 10, 2))
print(list10Asc)

# print 10 to 0 descending
list10Desc = list(range(10, 0, -2))
print(list10Desc)

# print 10 to 0 empty list as step is wrong
list10Empty = list(range(10, 0, 2))
print(list10Empty)