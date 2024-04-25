from functools import reduce 

num=[2,3,1,5,6]

total=reduce(lambda x,y:x+y, num)  #reduce(function, items of sequence)
print(total)