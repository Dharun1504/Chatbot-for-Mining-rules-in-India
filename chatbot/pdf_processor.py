from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
import os

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=4000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    vectorstore.save_local("Vectorstore")
    if(len(os.listdir("Vectorstore"))==0):
        return vectorstore
    else:
        c=FAISS.load_local("Vectorstore",embeddings=embeddings)
        return c

pdf_directory = "D:\sss"  
pdf_files = os.listdir(pdf_directory)
raw_text = ""
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)
    pdf_text = get_pdf_text([pdf_path])
    raw_text += pdf_text

text_chunks = get_text_chunks(raw_text)
vectorstore = get_vectorstore(text_chunks)


def reee():
    return vectorstore  