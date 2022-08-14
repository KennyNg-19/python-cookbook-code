'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:35:44
Description: 
'''
# Tricky initialization problem involving multiple inheritance.
# Does NOT use super()


class Base:

    def __init__(self):
        print('Base.__init__')


class A(Base):

    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):

    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


if __name__ == '__main__':
    # Please observe double call of Base.__init__
    c = C()
