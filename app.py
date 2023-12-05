import streamlit as st
from multiapp import MultiApp
# Import app modules
from apps import home, ReqSemSearch 

app = MultiApp()

# Plugin applications
app.add_app("NLP4RE Home Page", home.app)
app.add_app("Requirements Semantic Search", ReqSemSearch.app)


# Main app
app.run()