'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:03:39
Description: 
'''


class A:

    def __init__(self):
        self.x = 0


class B(A):

    def __init__(self):
        super().__init__()
        self.y = 1


if __name__ == '__main__':
    b = B()
    print(b.x, b.y)
