import pytest
import json
import os
import sys
from  main import add, length ,delete , complete
sys.path.insert(0,"../phase-0")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "test_tasks.json")
originalfile = "../phase-0/tasks.json"


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
    
@pytest.fixture
def emptylist():
     data = []
     with open(filename,"w") as file:
        json.dump(data,file,indent=4)
     



def test_add(emptylist):
  
    add("afolabi",filename)
    with open(filename,"r") as file:
            data = json.load(file)
            assert(data[0]["name"]=="afolabi") 

def test_delete(emptylist):
  
     add("afolabi",filename)
     len1 = length(filename)
     delete(1, filename)
     len2 = length(filename)
     assert(len1-1 == len2)

def test_complete(emptylist):
   
      add("afolabi",filename)
      complete(1, filename)
      with open(filename,"r") as file:
            data = json.load(file)
            assert(data[0]["completed"]== True) 




