'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:03:12
Description: 
'''


class A:

    def spam(self):
        print('A.spam')


class B(A):

    def spam(self):
        print('B.spam')
        super().spam()  # after, Call parent spam()


if __name__ == '__main__':
    b = B()
    b.spam()
