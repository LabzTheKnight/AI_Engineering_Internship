import json
import os
import sys
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")



def length(file_path = filename):
    with open(file_path,"r") as file:
        data = json.load(file)
        return len(data)
    
def add(a, file_path = filename):
    with open(file_path,"r") as file:
        data = json.load(file)
        index = len(data)+1
        task = {"index": index , "name" : a , "completed":False}
        data.append(task)
    with open(file_path,"w") as file:
        json.dump(data,file,indent = 4)

def list(file_path = filename):
    with open(file_path,"r") as file:
        tasks = json.load(file)
    for task in tasks:
        print(f"{task["index"]}. {task["name"]} {'true' if task["completed"] else 'false'}")

def complete(index , file_path = filename):
    with open(file_path,"r") as file:
        data = json.load(file)
        task = data[int(index)-1] 
        task["completed"] = True
        data[int(index)-1] = task
    with open(file_path,"w") as file:
        json.dump(data,file,indent=4)

def delete(index, file_path = filename):
    with open(file_path,"r") as file:
        data = json.load(file)
        data.pop(int(index)-1) 
        i = 1
        for task in data:
            task["index"]= i
            i+=1
    with open(file_path,"w") as file:
        json.dump(data,file,indent=4)
            

def main():
    function =sys.argv[1]
    match function:
        case "add":
            if sys.argv[2]:
                add(sys.argv[2])
            else:
                print("no argument")
        case "list":
            list()
        case "complete":
            complete(sys.argv[2])
        case "delete":
            delete(sys.argv[2])

if (__name__ == "__main__"):
    main()