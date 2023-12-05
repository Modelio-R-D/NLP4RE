import io
import fitz 
import re
import pandas as pd
import spacy
import string
import streamlit as st
from collections import Counter
from typing import List, Optional
from unicodedata import normalize

FOOTER_PATTERN = re.compile(r'Page\s+\d+\s+of\s+\d*', re.IGNORECASE)
LIST_PATTERN = re.compile(r'^[a-zA-Z]\.|^([0-9]*\.[0-9]*)+')
END_OF_SENTENCE_CHARACTERS = {'.', '?', '!'}

def is_header(s):
    return s.count(".") > 10

def preprocess(s):
    s = re.sub(LIST_PATTERN, "", s)
    return s.strip()

def is_footer(s):
    return re.search(FOOTER_PATTERN, s) 

def prefilter_line(line: str):
    return not is_footer(line) and not is_header(line)

def is_camel_case(s):
    return s != s.lower() and s != s.upper()

def merge_next_line(line_1: str, line_2: str) -> bool:
    return len(line_1) > 30 and not line_1.isupper() and \
           line_1.strip()[-1] not in END_OF_SENTENCE_CHARACTERS and \
           any(char.isalpha() for char in line_2) and \
           not all(map(is_camel_case, line_1))

def filter_line(line: str):
    return line and len(line.split()) > 3 and len(line.strip()) > 30 \
           and any(char.isalpha() for char in line) and not is_footer(line) and \
           all(char in string.printable for char in line)

def load_spacy_model(name="en_core_web_sm"):
    if not spacy.util.is_package("en_core_web_sm"):
        spacy.cli.download('en_core_web_sm')
    nlp = spacy.load(name)
    return nlp

st.cache(ttl=60*5,max_entries=20)
def retrieve_sentences_from_lines(lines: List[str]) -> List[str]:
    nlp = load_spacy_model()
    extracted_sentences = []
    for line in lines:
        doc = nlp(line)
        sentences = [subsentence.strip() for sentence in doc.sents for subsentence in sentence.text.split('\n')]
        relevant_sentences = filter(filter_line, sentences)
        extracted_sentences.extend(relevant_sentences)
    filtered_sentences = map(preprocess, extracted_sentences)
    filtered_sentences = list(set(filtered_sentences))
    return filtered_sentences

st.cache(ttl=60*5,max_entries=20)
def retrieve_lines_from_pdf_file(file_buffer: Optional[io.BytesIO]=None) -> List[str]:
    if not file_buffer:
        return []
    doc = fitz.open(None, file_buffer, filetype="pdf")
    lines = [line.strip() for page in doc for line in page.get_text("text").split("\n") if line.strip()]
    
    repeats_counter = Counter(lines)
    lines = [normalize('NFKC', line) for line in lines if repeats_counter[line] < doc.pageCount / 2] # delete headers

    lines = list(filter(prefilter_line, lines))
    lines = list(map(preprocess, lines))
    concatenated_lines = [lines[0]]
    for i in range(1, len(lines)):
        line_1_text = concatenated_lines[-1]
        line_2_text = lines[i]
        merge = merge_next_line(line_1_text, line_2_text)
        if not merge:
            concatenated_lines.append(line_2_text)
            continue
        if line_1_text[-1] == "-":
            concatenated_lines[-1] = f"{line_1_text[:-1]}{line_2_text}" 
        else:
            concatenated_lines[-1] = f"{line_1_text} {line_2_text}"
    filtered_lines = list(filter(filter_line, concatenated_lines))
    return filtered_lines
  
@st.cache(ttl=60*5,max_entries=20)
def process_file(file_buffer: Optional[io.BytesIO]=None) -> List[str]:
    lines = retrieve_lines_from_pdf_file(file_buffer)
    sentences = retrieve_sentences_from_lines(lines)
    dataframe = pd.DataFrame(sentences, columns=["Text"])
    return dataframe