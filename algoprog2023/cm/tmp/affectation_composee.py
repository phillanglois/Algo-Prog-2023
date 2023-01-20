'''
Comparaison de comportement python3.7 et jupyter notebook kernel 3.7
L'affectation composée est sensée se dérouler en place
'''
# a et b non mutables
a = 0
b = 11
print(id(a), id(b))

a += 1
b = b + 1
print(id(a), id(b))

# a et b mutables
a = [0]
b = [11]
print(id(a), id(b))

a += [1]
b = b + [1]
print(id(a), id(b))
