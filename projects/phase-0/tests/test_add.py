import pytest
import json
import os
import sys
sys.path.insert(0,"../phase-0")
from  main import add, length


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "test_tasks.json")
originalfile = "../phase-0/tasks.json"
class TaskList():
    def __init__(self):
         self.list = []

class Task():
     def __init__(self,name):
          self.name = name 

@pytest.fixture
def test_List():
    with open(originalfile,"r") as file:
        data= json.load(file)
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)

         
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

def test_list_not_empty(test_List):
     pass
