import langchain
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore


vector_stores = InMemoryVectorStore(Ollama_Embeddings)

Ollama_Embeddings = OllamaEmbeddings(model="qwen3:4b")

def chunk(docs: list):
    text_splitter = RecursiveCharacterTextSplitter(chuck_size=100, chunk_overlap=200)
    split_docs = text_splitter.split_documents(docs)
    return split_docs

