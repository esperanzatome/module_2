#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

listado = ['z', 'y', 'x']
tuples = (4, 5, 6)
float_number = 5.5
integer_number = 5

from decimal import Decimal

decimal_number = Decimal(5.678776765)
print(decimal_number)

dictionary = {'a': '1º', 'b': '2º', 'c': '3º'}

#Exercise 2: Round your float up.

round(float_number)
print(round(float_number))

#Exercise 3: Get the square root of your float.

import math

math.sqrt(float_number)
print(math.sqrt(float_number))

#Exercise 4: Select the first element from your dictionary.

dictionary.get('z')
print(dictionary.get('z'))

#Exercise 5: Select the second element from your tuple.

tuples[1]
print(tuples[1])

#Exercise 6: Add an element to the end of your list.

listado += ['w']
print(listado)

#Exercise 7: Replace the first element in your list.

listado[0] = 'zeta'
print(listado)

#Exercise 8: Sort your list alphabetically.

sorted(listado)
print(sorted(listado))

#Exercise 9: Use reassignment to add an element to your tuple.

tuples += (7, )
print(tuples)
