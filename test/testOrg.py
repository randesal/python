print('Enter lot number:')
import os
x = input()
sPath =  '\\\\192.168.1.75\\file server\\Backend-test\\test e-map\\_EMap Data\\' + x
print(sPath)

f = open(sPath, "r")

print(f.read())
"\\192.168.1.75\file server\Backend-test\test e-map\0123D292\00740D-0123D292-001.txt"s= input()