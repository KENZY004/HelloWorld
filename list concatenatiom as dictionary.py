#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kenzn
#
# Created:     30-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list1=input("data1: ").split(",")
list2=input("data2: ").split(",")
if len(list1)!=len(list2):
    print("lists afre different length")
else:
    outstr="{"
    for i in range(len(list1)):
        outstr +=f"'{list1[i]}':'{list2[i]}',"
        outstr=outstr[:-2]
        outstr+="'}"
        print(outstr)