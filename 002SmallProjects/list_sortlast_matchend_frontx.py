#! /usr/bin/python3

#name: Kenneth Zeng  
#date:05/29/2020

'''
match_end(): compare the first and last char of each element in given list of string. 

front_t(): return a list with the strings in sorted order, except group all the strings that begin with 'x' first.

sort_last(): Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple
'''

def match_end(words):
    count = 0
    for word in words:
        if len(word) >=2 and word[0] ==word[-1]:
            count += 1

    return count 

#['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] =>['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
def front_x(words):
    x_list =[]
    rest_list =[]
    for word in words:
        if word.startswith('x') or word.startswith('X'):
            x_list.append(word)
        else:
            rest_list.append(word)
    return sorted(x_list) + sorted(rest_list)

'''
another approach: create another list ans =[] which have the same size as list words. 
                soreted list words 
                started from last element of list. 
                     if the word start with x, skip first 
                     if the word not start with x, place it at last postion. iterate it 
                now you append last element of sorted list word(the word with x in last position) for continue 

one more approach: sorted the list words 
                start from back of list, find and locate the start index of word which start x
                start from that index until the end, append it to new list; then append the word start from index 0 of words list before reach word started with x

'''

def last(a):
    return a[-1]

def sort_last(tuples):
    return sorted(tuples, key=last)
    #don't do below, wrong output; not the same result 
    #sorted(tuples, key=last)
    #return tuples

#test function: what each function vs. what it's supposed to return 
def test(got, expected):
    if got == expected:
        prefix ='ok'
    else: 
        prefix = ' X '
    print('%s  got: %s expected: %s ' %(prefix, got,expected ))
     
#create test cases 
def main():
    print("validating test cases for match_end()")
    list1 = ['aba', 'xyz', 'aa', 'x', 'bbb' ]
    list2 =['', 'x', 'xy', 'xyx', 'xx']
    list3 = ['aaa', 'be', 'abc', 'hello']
    test(match_end(list1), 3)
    test(match_end(list2), 2)
    test(match_end(list1), 1)
    print('\n')

    print('Validating front_x test cases')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    print('\n')

    print('Validating sort_last test cases')
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),[(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__=='__main__':
    main()



'''
output for match_end()
ok  got: 3 expected: 3 
ok  got: 2 expected: 2 
 X   got: 3 expected: 1 

output for front_x
Validating front_x test case
ok  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] 
ok  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] 
ok  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']


ok  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)] 
ok  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)] 
ok  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] 
'''