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

def ai_summarize(content: str) -> str:
    return "summarized"

def ai_gen_quiz( content: str ) -> str:
    return "quiz"