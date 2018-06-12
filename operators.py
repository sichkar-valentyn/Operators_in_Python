# File: operators.py
# Description: Examples how to use operators in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples how to use operators in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Operators_in_Python (date of access: XX.XX.XXXX)


import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4))

x = [1, 2, 3]
f = op.itemgetter(1)  # f(x) == x[1]
print(f(x))

y = {'123': 3}
f = op.itemgetter('123')
print(f(y))
