Phase 0:
    Task 0.1: Build a CLI todo app in Python.
    Task 0.2: Add file storage with JSON.
    Task 0.3: Add unit tests.
    Task 0.4: Dockerize it.
    Task 0.5: Write a README like a real open-source project.

built basic CRUD 

i have the pthyon basic script running now i would like to make a venv and add a json file to make the bd persistant

using the json library i can manipulate json in pyhton although the i have to copy and delete the json file everytime i update it (need to check if that i the only way)

sys and sys.argv to work with cli arguments as strings

this part of the code is necessary so that the compiler know to run what every function is named main() in your app
if (__name__ == "__main__"):
    main()

now i am trying to implement tests with pytest. its seem to work by making an object to represent changes that goes on after running functions and test the the object attribute are as they should be