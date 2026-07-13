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

**TECHINCAL DEBT**

    main.py is doing too much. Later, split into database.py, models.py, schemas.py, and routes.py.
    read_root() returns a set-like value. It should become a normal JSON object.
    update_item() does not handle “task not found” before setting completed.
    Tests cover happy paths, but not enough failure paths: missing item, invalid ID, empty title, delete nonexistent item.
    Test file should eventually be renamed from test.py to something clearer like test_tasks.py.
    Your database URL is hardcoded. Later, use environment variables.
    Docker uses --reload, which is good for development but not production.
    SQLite volume is working conceptually, but you should document where the DB lives inside the container.
    CI installs pytest separately even though test dependencies should ideally be in requirements or a dev requirements file.
    No auth yet, even though it was in the Phase 1 roadmap. It is okay to defer, but mark it as debt.
    No README explaining how to run Phase 1 locally, with Docker, and with tests.