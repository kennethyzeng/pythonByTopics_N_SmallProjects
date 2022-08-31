import copy

li1 = [1, 2, [3,5], 4]
  
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ") 
print("\r")
  
# adding and element to new list
li2[2][0] = 7
  
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")  
print("\r")
  
# Change is NOT reflected in original list as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")