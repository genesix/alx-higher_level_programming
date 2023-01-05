#!/usr/bin/python3

my_square = Square()
Square = __import__('0-square').Square

print(type(my_square))
print(my_square.__dict__)
