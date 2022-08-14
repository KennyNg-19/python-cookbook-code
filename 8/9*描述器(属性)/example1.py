'''
Author: kenny_wu
Date: 2022-08-08 13:02:22
LastEditors: kenny_wu
LastEditTime: 2022-08-14 22:48:47
Description: 
'''

# Descriptor attribute for an integer type-checked attribute

# 描述器通常是那些使用到装饰器或元类的大型框架中的一个组件


# 如果你只是想简单的自定义某个类的单个属性访问的话就不 用去写描述器了。
# 这种情况下使用 8.6 小节介绍的 property 技术会更加容易描述器通常是那些使用到装饰器或元类的大型框架中的一个组件
class Integer:
    def __init__(self, name):
        self.name = name

    """
    __dict__ 是 
    描述器的 self.name 属性存储了在实例字典中 被实际使用到的 key。
    """

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.x)
    p.y = 5
    try:
        p.x = 2.3
    except TypeError as e:
        print(e)
