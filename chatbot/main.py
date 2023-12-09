import streamlit as st
from dotenv import load_dotenv
from vect import ree

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import os

most_used_queries = [
    "What are the key acts and regulations governing coal mining in India?",
    "How can I apply for coal mining licenses or permits in India?",
    "What is the process for obtaining a coal mining lease in India?",
    "What is the status of coal block auctions in India?",
    "What is the role of the Coal Controller's Organization in India?"
]


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})


    st.write(user_template.replace("{{MSG}}", user_question), unsafe_allow_html=True)

    
    st.write(bot_template.replace("{{MSG}}", response['chat_history'][-1].content), unsafe_allow_html=True)


def main():
    load_dotenv()

    st.set_page_config(
        page_title="Chatbot for Mining Rules", page_icon="⛏️")
    st.write(css, unsafe_allow_html=True)
    vectorstore = ree()

    st.session_state.conversation = get_conversation_chain(
        vectorstore)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    header_style = """
    <style>
    .custom-header {
        font-size: 20px; 
    }
    </style>
    """
    st.markdown(header_style, unsafe_allow_html=True)
    st.markdown("<p class='custom-header'>Greetings! I'm your coal-mining companion, ready to delve into the depths of your coal mining-related queries with expertise and enthusiasm</p>", unsafe_allow_html=True)

    
    user_question = ""

    
    with st.form(key='user_input_form',clear_on_submit=True):
        user_question = st.text_input("How can I assist you today?",key="widget")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button and user_question:
           
            
            handle_userinput(user_question)
            user_question = ""  



if __name__ == '__main__':
    main()
