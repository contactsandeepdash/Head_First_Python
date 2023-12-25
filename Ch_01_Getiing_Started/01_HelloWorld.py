# print hello world
print ("hello world")

# check for current working directory
from os import getcwd
where_am_i = getcwd()
print ("current location -- : " + where_am_i)

# check for current working directory
import os
print ("current location ## : " + os.getcwd())
print (os.getenv('SHELL'))
print ("env variables ## : " + str(os.environ))

# check for current platform
import sys
# below will print Darwin - the Mac OS X kernel name
print (sys.platform)
print (sys.version)
print (sys.version_info)