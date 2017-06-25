#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from mypackage.my_utils import utils
from  mypackage.my_utils import MyClass

'''
每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
'''
if __name__ == "__main__":
    #调用模块的全局函数
    utils()
    #调用模块的Class member func 
    mu = MyClass()
    mu.class_utils()
