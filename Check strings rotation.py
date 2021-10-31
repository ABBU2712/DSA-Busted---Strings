def is_rotation(str1,str2):
    temp=''
    if len(str1) != len(str2):
        return 0
    temp=str1 + str1
    if temp.count(str2) > 0:
        return 1
    else:
        return 0

str1 = "ABCD"
str2 = "CDAB"

if is_rotation(str1, str2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")