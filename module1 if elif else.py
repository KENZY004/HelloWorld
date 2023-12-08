#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     15-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=int(input("a: "))
b=int(input("b: "))
if((a==6) | (b==6)):
    print("true")
elif((a+b==6) | (a-b==6)):
    print("true")
else:
    print("false")

