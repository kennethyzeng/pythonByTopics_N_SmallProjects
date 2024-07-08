import timeit 
##example 1:
print(timeit.timeit('char in text', setup ='text="sample string"; char="g"') )  #beware of '' and " "; faster

print(timeit.timeit('text.find(char)', setup='text="sample string"; char="g"'))   ##slower


#example 2 can be done with Timer
t = timeit.Timer('char in text', setup ='text="sample string"; char="g"')   
print(t.timeit())

###reapte the same process. list each measurement in array
print(t.repeat())
print(t.repeat(10))  #10 times