import pytest
import json
import os
import sys
sys.path.insert(0,"../phase-0")
from  main import add, length

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")
class TaskList():
    def __init__(self):
         self.list = []

class Task():
     def __init__(self,name):
          self.name = name 


@pytest.fixture
def currentList():
    with open(filename,"r") as file:
            data = json.load(file)
            return data

def test_add():
    len1=length()
    add("afolabi")
    len2=length()
    assert(len1+1==len2)
    