
from functools import reduce
# Lamda
square  = lambda x: x *x
print(square(5))

#map(), filter(), reduce()


numbers = [1,2,3,4, 5, 6]
#Square of numbers
squares = list(map(lambda x: x**2, numbers))
print(squares)

#Cubes of numbers
cubes = list(map(lambda x: x**3, numbers))
print(cubes)

#filter
# filter the even numbers out of list
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

#filter out number which are > 2
greaterThan2 = list(filter(lambda x: x>=2, numbers))
print(greaterThan2)


#reduce
product = reduce(lambda x, y: x+y, numbers)
print(product)

product = reduce(lambda x, y: x*y, numbers)
print(product)