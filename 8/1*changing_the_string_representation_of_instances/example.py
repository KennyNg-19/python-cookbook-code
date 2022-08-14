'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:25:04
Description: 
'''


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        print('run __repr__')
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        print('run __str__')
        return '({0.x}, {0.y})'.format(self)


print(Pair(1, 2))
