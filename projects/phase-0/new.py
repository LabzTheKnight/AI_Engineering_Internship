import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")
originalfile = "tests/tes"



def test_List():
    with open(originalfile,"r") as file:
        data= json.load(file)
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)