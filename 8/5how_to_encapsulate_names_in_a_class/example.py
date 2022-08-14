'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:12:35
Description: 
'''
# Example of using __ method name to implement a
# non-overrideable method


class B:

    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print('B.__private_method', self.__private)

    def public_method(self):
        self.__private_method()


class C(B):

    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        print('C.__private_method')


c = C()
c.public_method()
