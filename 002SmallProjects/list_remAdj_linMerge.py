#! /usr/bin/python3

#name: Kenneth Zeng  
#date:05/29/2020

'''
remove_adjacent(): remove repeated adjacent number/s and reduce to be single element in list 

liner_merge(): Given two lists sorted in increase order, merge them to become a single list in sorted order 

'''

def remove_adjacent(nums):
    ans = []
    for num in nums:
        if len(ans)==0 or num != ans[-1]:
            ans.append(num)
    return ans
#another approach: use two pointers i,j; j moves forward, skip the repeat ones; relocate i when the number at j is not a repeated number 

def linear_merge(input1, input2):
    ans = []
    while len(input1) and len(input2):
        if input1[0] < input2[0]:
            ans.append(input1.pop(0))
            #print(input1)
        else:
            ans.append(input2.pop(0))
            #print(input2)
    
    ans.extend(input1)
    ans.extend(input2)
    return ans


#test function: what each function vs. what it's supposed to return 
def test(got, expected):
    if got == expected:
        prefix ='ok'
    else: 
        prefix = ' X '
    print('%s  got: %s expected: %s ' %(prefix, got,expected ))

def main():
    print("validating remove_adjacent test cases")
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    print("\n")

    print("Validating linear_merge test case")
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()