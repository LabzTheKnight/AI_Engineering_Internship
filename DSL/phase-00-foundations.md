Phase 0:
    Task 0.1: Build a CLI todo app in Python.
    Task 0.2: Add file storage with JSON.
    Task 0.3: Add unit tests.
    Task 0.4: Dockerize it.
    Task 0.5: Write a README like a real open-source project.


recipe to build a python docker crud cli:

make a DB tasks.json
interface with DB with import json (json.load,dump etc file) interface with files "with open(filepath, "W")"
crud funtion to interact with files
main() with sys to interact with cli(systems arguments as strings)
if (__name__ == "main"): 
    main() to call the main function

recipe for testing:

import the functions you would like to test 
import pytest
pytest has a fixture attribute that make funtion that run everytime you can pass them into individual test so that they make changes before running the test ie (emptyList()) you run pytest
make a test fumctions that assert end values of a reference object

Technical debt todo:

fix broad except: handling
improve CLI argument validation
make tests run from repo root
clean up Dockerfile naming and volume docs
write a proper Phase 0 README
remove/ignore generated files
improve your DSL notes