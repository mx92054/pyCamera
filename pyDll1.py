import os
import sys
from ctypes import *

test = cdll.LoadLibrary('F:\VcProj\TestDll\Debug\TestDll.dll')
i = test.Add(1, 2)
print("result is %d" % i)
