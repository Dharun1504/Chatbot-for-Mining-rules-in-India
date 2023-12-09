from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
def ree():
    embeddings=OpenAIEmbeddings()
    c=FAISS.load_local("Vectorstore",embeddings=embeddings)
    return c


