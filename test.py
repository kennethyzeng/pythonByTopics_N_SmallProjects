def last(a):
    return a[-1]

def sort_last(tuples):
    print(sorted(tuples, key=last))
    #print(tuples)

list = [(1, 3), (3, 2), (2, 1)]
sort_last(list)
print(list)
print(sorted(list))
