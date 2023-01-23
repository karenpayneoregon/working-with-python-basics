#
# Import a standard module for working with dates
#
from datetime import date

print("Greetings from module 1")

today = date.today()
print("Today's date:", today)
print("")
#from pythonnet import load
import clr
clr.AddReference('PythonOedLibrary')
from PythonOedLibrary import EnvironmentOperations

print(EnvironmentOperations.Hello("Karen"))

from json1 import JsonWork
JsonWork.Example()
print


