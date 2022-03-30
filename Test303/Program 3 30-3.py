ìnput1 = float(input('Input the first string : '))
ìnput2 = float(input('Input the second string: '))
false = 'They are not identicle!'
true = 'They are identicle!'
def str_comp(i1, i2):
    if i1 == i2:
        return true
    else:
        return false
print(str_comp(ìnput1, ìnput2))