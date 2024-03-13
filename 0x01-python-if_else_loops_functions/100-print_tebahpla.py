#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    if i % 2 == 0:
        ch = 0
    else:
        ch = 32
    print('{}'.format(chr(i - ch)), end='')
