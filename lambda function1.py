#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     19-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

tax1= lambda salary:salary*20/100
salary=float(input("please enter your salary:"))
print("tax to be paid is ",tax1(salary))