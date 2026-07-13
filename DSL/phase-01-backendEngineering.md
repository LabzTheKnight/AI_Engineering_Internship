CLI app:
user -> terminal command -> Python function -> JSON file

API app:
user/client -> HTTP request -> route function -> database -> HTTP response

Create a minimal FastAPI app.
Add one health route: GET /health.
Add in-memory notes CRUD first.
Then replace in-memory storage with SQLite.
    sqlalchemy library: engine and session(orm) through helper functions.
        create_engine("location of the db = sqlite.....")
        create session and bind to engine
        create declarative base 
        create a class of the item you would you like to store and pass the base as an argument
        def get_db() : yield local db session and close at the end
            this must be passed to every api call that need db info 
Add request/response models with Pydantic.
    pydantic library: BaseModel
        this steps lets us setup the shape of the object we are sending and recieveing request with 
        class Task(BaseModel) 
Add tests.
    create a testclient with the TestClient from the fastapi library
    create an engine in memory with static pool so it know to always connect to the same db in memory
    create a testing local session
    overide get_db so db = testingSessionLocal
    make a fixture to create table , yields (return to the test) and teardown tables after the test
    write test that assert that the response object matches your expectation
Add Docker.
    describe the image
        working environment ie linux etc
        the name of the root dir of the container
Add Docker Compose.
    define the services and volumes to be used
    the service could be pulled from exitsting images or not. define the **ports** and other services it may *depend*  on 
Add simple auth.
Add GitHub Actions CI.
Do not start with Postgres. Start with SQLite so you understand the backend shape first. Postgres can come after you understand routes, models, persistence, and tests.

Your first Phase 1 learning question should be:

What is the difference between a CLI command and an HTTP request?