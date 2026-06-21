import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")
originalfile = "tests/tes"
import json
import sys
sys.path.insert(0,"../phase-0")
from  main import add, length ,delete , isno


def emptylist():
     data = []
     with open(filename,"w") as file:
        json.dump(data,file,indent=4)


delete("1")
