import streamlit as st

def app():
    st.title('NLP4RE Prototype')

    st.write(
                """
    This application aims at using Natural Language Processing (NLP) techniques for Reequirements Engineering (RE), or NLP4RE for short. Currently, it offers a prototype called "Requirements Semantic Search" that evaluates semantic similarity of requirement text, and thus can be used for semantic search of a given requirement in a large requirements document.
    
    The NLP4RE Prototype is designed for use in RE case studies where businesses and industries are studying recurrent clients' bids or tender with relatively similar or standard requirements specification documents and who are interested in providign their RE teams with insights on new projects based on responses to previous ones.  For instance, it helps RE teams while studying new bid and tender documents by identifying similar requirements from previous projects, and thus to tackle and answer the new requirements based on answers to the previous similar ones (e.g., allocate similar requirements to similar teams, respond to requirements compliance similarly, etc.).
        
    This application was developed by Bilal Said from the Modelio R&D Team at Softeam Docaposte, within the framework of the AIDOaRt EU collaborative research project, and applied on datasets provided by Alstom AB (previously Bombardier Transportation or BT) on railway systems tender documents, and HI iberia Ingenieria Y Proyectos SL (HIB) on Trello cards for software development, provided in Spanish.
    
    The NLP4RE Prototype is planned for integration in Modelio in case of validation for commercial use by the Modelio Core Development Team.
    
    The code base has been inspired from prototypes developed by the Modelio R&D Team for the VeriDevOps research project, namely by Kirill Yakovlev, Andrey Sadovykh, and Alexander Naumchev.

    This prototype application is still a work in progress and shall be updated with more features in the future.        
    
    Updates (Dec 2023):
    - Release as a runnable web application
    
    Next:
    - Containerization with Docker
    - Separate the web back-end (Flask or FastAPI) and front-end (streamlit)
        """
        )