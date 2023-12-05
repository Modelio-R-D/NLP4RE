# NLP4RE
This application aims at using Natural Language Processing (NLP) techniques for Requirements Engineering (RE), or NLP4RE for short. Currently, it offers a prototype called "Requirements Semantic Search" that evaluates semantic similarity of requirement text, and thus can be used for semantic search of a given requirement in a large requirements document.
    
The NLP4RE Prototype is designed for use in RE case studies where businesses and industries are studying recurrent clients' bids or tender with relatively similar or standard requirements specification documents and who are interested in providign their RE teams with insights on new projects based on responses to previous ones.  For instance, it helps RE teams while studying new bid and tender documents by identifying similar requirements from previous projects, and thus to tackle and answer the new requirements based on answers to the previous similar ones (e.g., allocate similar requirements to similar teams, respond to requirements compliance similarly, etc.).


## Roadmap
This prototype application is still a work in progress and shall be updated with more features in the future.        
    
**Updates (Dec 2023):**
- Release as a runnable web application
- Containerization with Docker
    
**Next:**
- Separate the web back-end (Flask or FastAPI) and front-end (streamlit)


## Prerequisites
```
Python 3.8-3.9
```

## How to Run

1. Clone the repository:
```
$ git clone TODO
$ cd NLP4RE
```

2. Install dependencies:
```
$ pip install -r requirements.txt
```

3. Start the application:
```
streamlit run app.py
```

OR 

If you want to specify port number (e.g. port #8502):
```
streamlit run app.py --server.port 8502
```

## Notes
First launch might take some time to download all necessary NLP models and libraries which allocate ~750 Mb of extra disk space.

## Credits        
This application was developed by Bilal Said within the framework of the AIDOaRt project, and applied on datasets provided by Alstom (BT) on railway systems tender documents, and HI iberia Ingenieria Y Proyectos SL (HIB) on Trello cards in Spanish. The NLP4RE Prototype is planned for integration in Modelio in case of validation for commercial use by the Modelio Core Development Team.
    
The code base has been inspired from prototypes developed for the VeriDevOps project by Kirill Yakovlev, Andrey Sadovykh, and Alexander Naumchev.
