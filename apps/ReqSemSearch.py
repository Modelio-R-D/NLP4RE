import os
import pandas as pd
import numpy as np
import streamlit as st
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from utils.utils import process_file
from PIL import Image


def set_header():
    path = os.path.dirname(__file__)
    col1, col2, col3 = st.columns(3)

    with col1:    
       image = Image.open(path+'/Softeam.png')
       st.image(image)

    with col2:
       image = Image.open(path+'/AIDOaRt.png')
       st.image(image)       

    with col3:
       image = Image.open(path+'/ALSTOM.png')
       st.image(image)    

    st.title("**Requirements Semantic Search**")
    init_sent = st.text_area('Input one or more requirements here:') 
    uploaded_file = st.file_uploader("Choose a document", type=['pdf'])
    int_val = st.number_input('Desired number of similar requirements to find', min_value=1, max_value=10, value=5, step=1)
    return int_val, uploaded_file, init_sent


def show_extracted_sentences(count, init_req, reqs) :
    if reqs.shape[0] == 0:
        st.markdown(init_req)
        st.markdown("### No relevant requirements have been found###")
    else:
        st.markdown("### Requirement #" + str(count))
        st.markdown(init_req[0])
        st.markdown("### Similar requirements for #" + str(count))
        for i, req in enumerate(reqs) :
            st.markdown(str(i+1) + '-' + req)


def preparing_model():
    model = SentenceTransformer('all-mpnet-base-v2')
    return model

def app():
    count = 0
    int_val, uploaded_file, init_sent = set_header()
    model = preparing_model()
    start = st.button('Start')
    if start:
        if uploaded_file is not None and init_sent is not None:
            reqs_split = init_sent.split("\n")
            sents_from_doc = process_file(uploaded_file.getvalue())
            for req in reqs_split:
                count += 1
                embedding_sent = model.encode([req], convert_to_tensor=True)
                embeddings_sents = model.encode(sents_from_doc['Text'], convert_to_tensor=True)
                cos_scores = cosine_similarity(embedding_sent, embeddings_sents)
                sorted_ = np.argsort(-cos_scores)[0][:int_val]
                show_extracted_sentences(count, [req], np.array(sents_from_doc["Text"])[sorted_])