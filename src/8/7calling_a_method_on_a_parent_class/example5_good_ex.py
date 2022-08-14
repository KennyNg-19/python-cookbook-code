'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:35:59
Description: 
'''
# Tricky initialization problem involving multiple inheritance.
# Uses super()


class Base:

    def __init__(self):
        print('Base.__init__')


class A(Base):

    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):

    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):

    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


if __name__ == '__main__':
    # Observe that each class initialized only once
    c = C()
