import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(
    model = "qwen3:4b",
    temperature = 0
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system","You summarize user notes accurately."
        ),
        (
            "human", "Summary style: {style} Note: {note}"
        )

    ]
    )

summary_chain = prompt | model

prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You generate a quiz from the note"),
        ("human", "Quiz style: {style} Note: {note}")
    ]
)

quiz_chain = prompt2 | model

def ai_summarize(content: str) -> str:
    return "summarized"

async def ai_gen_quiz( content: str ) -> str:
    result = await quiz_chain({"note":content , "style": "brief"})
    return result