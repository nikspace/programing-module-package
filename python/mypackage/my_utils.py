#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mypackage
'''

def utils():
    print ("mypackage.my_utils.utils() called ")

class MyClass(object):
    def class_utils(self):
        print("mypackage.my_utils.MyClass.class_utils() called")
