An LLM app is a normal software app where one part of the logic is delegated to a model through a prompt.
The engineering work is controlling inputs, prompts, outputs, errors, cost, and persistence.
i am using the langchain lib to handle the prompting:
    spicify the model and temperature(ai jargon) 
    use prompt template to make system prompt and human prompt(what you expect to get from the api call)
    make a chain which is usual a prompt piped to a model .
    invoke the chain with the human input in the format it expects.
TECHNICAL DEBT:
find a way to make local model talk with api container