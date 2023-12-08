#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kenzn
#
# Created:     01-11-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#----------------------------------------------------------------------------
data=input("data:")
tuple1=tuple(data.split(","))
a=min(tuple1)
print("min:",a)
#or data=tuple(map(int,input("data: ").split(",")))
#a=min(data)
#print("min:",a)