#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     20-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-----------------------------------------------------------l
list1=[1,2,3,4,5]
def squares():
    return x**2
print(list(map(squares,list1)))
print(list(map(lambda x: x**2,list1)))
print([x**2 for x in list1])