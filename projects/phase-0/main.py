import json
import os
import sys
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")



def length(file_path = filename):
    try:
        with open(file_path,"r") as file:
            data = json.load(file)
            return len(data)
    except:
        FileNotFoundError("file path wrong")

def add(a, file_path = filename):
    try:
        with open(file_path,"r") as file:
            data = json.load(file)
            index = len(data)+1
            task = {"index": index , "name" : a , "completed":False}
            data.append(task)
        with open(file_path,"w") as file:
            json.dump(data,file,indent = 4)
    except:
        FileNotFoundError("input most be a string or invalid filepath")

def list(file_path = filename):
    try:
        with open(file_path,"r") as file:
            tasks = json.load(file)
        for task in tasks:
            print(f"{task["index"]}. {task["name"]} {'true' if task["completed"] else 'false'}")
    except:
        FileNotFoundError("invalid file path")

def complete(index , file_path = filename):
    try:
        with open(file_path,"r") as file:
            data = json.load(file)
            if length(file_path) >= int(index)>0:
                task = data[int(index)-1]
                if task["completed"]:
                    raise ValueError("task is already completed try another task") 
                task["completed"] = True
                data[int(index)-1] = task
            else:
                raise IndexError("task does not exist in list") 
            
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)
    except:
        raise FileNotFoundError("Index input most be integer or invalid file path")

def delete(index, file_path = filename):
    try:
        with open(file_path,"r") as file:
            data = json.load(file)
            if length(file_path) >= int(index)>0:
                data.pop(int(index)-1)
            else:
                raise IndexError("task does not exist in list") 
            i = 1
            for task in data:
                task["index"]= i
                i+=1
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)
    except:
        raise FileNotFoundError("Index must be an int or file path is invalid")  

def isno(op):
    for number in op:
        return number in "1234567890"      

def main():

    function = sys.argv[1]
    if function not in ["add","list","complete","delete"]:
        raise ValueError("not a recognised fuction")
    match function:
        case "list":
            list()
            return

    if sys.argv[2]:
        opperand = sys.argv[2]
        match function:
            case "add":
                if opperand == "":
                    raise ValueError("task can't be empty")
                else:
                    add(opperand)
            case "complete":
                if length() >= int(opperand) >=1 and isno(opperand):
                    complete(opperand)
                else:
                    raise IndexError("task isn't in the task list")
            case "delete":
                if length() > 0 and isno(opperand):
                    delete(opperand)
                else:
                    raise IndexError("There are not task matches that index")
    else:
        raise ValueError("the method requires a task or task index")         


if (__name__ == "__main__"):
    main()