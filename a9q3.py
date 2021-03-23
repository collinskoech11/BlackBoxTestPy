def hasMajority ( ls ):
’’’
Determines if the input list " ls " includes the majority element or not .
: param ls : an arbitrary list with comparable elements
: return : True if the input list has a majority element ; False otherwise .
’’’
# initialize the dictionary with keys are the elements in ls ,
# and values are the count the key in ls .
counts = {}
# update the dictionary of counts by loop in the list
for i in ls :
if i in counts :
counts [ i ] += 1
else :
counts [ i ] = 0
# generate the max count of all values in the list
max_count = max ( counts . values ())
# generate the result
result = max_count > len ( ls )//2
return result
isMajorityList ([1 ,2 ,3 ,1 ,1])