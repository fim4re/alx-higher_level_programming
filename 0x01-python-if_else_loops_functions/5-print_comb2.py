#!/usr/bin/python3
for number in range(100):
    print('{:02}'.format(number), end='\n' if number == 99 else ', ')
