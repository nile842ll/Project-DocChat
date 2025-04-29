from groq import Groq
from dotenv import load_dotenv
import os
import pdfplumber
from bs4 import BeautifulSoup
import argparse
import requests 
import sys

"""
.venv/bin/python docchat.py
"""

load_dotenv()
client = Groq(api_key=os.getenv("GroqAPIKEY"))

'''
def test_read_pdf_file(path):
    text = ''
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text
'''

def test_read_file(path):
    with open(path, "r") as file:
        text = file.read()
    return text

def test_read_html_file(path):
    text = ''
    with open(path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
    return text

def read_website(url):
    try: 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text   
    except Exception as e:
        print("failtoread", url, e)



def load_text(filepath_or_url):
    if ".pdf" in filepath_or_url:
        return test_read_pdf_file(filepath_or_url)
    if ".txt" in filepath_or_url:
        return test_read_file(filepath_or_url)
    if ".html" in filepath_or_url:
        return test_read_html_file(filepath_or_url)
    if "https" in filepath_or_url and not ".jpg" in filepath_or_url:
        return read_website(filepath_or_url)


def chunk_text_by_words(text, max_words=100, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0,len(words), max_words-overlap):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

#this finds same overlapping words only , not synonyms 
def score_chunk(chunk, query):
    chunkwords = chunk.split()
    querywords = query.split()
    commonwords = set(chunkwords).intersection(set(querywords))
    similarity = len(commonwords)/max(len(chunkwords), len(querywords))
    return similarity


def find_relevant_chunks(text, query, num_chunks=5):
    chunks = chunk_text_by_words(text, 20, 10)
    scores = []
    for chunk in chunks:
        chunkscore = score_chunk(chunk, query)
        scores.append((chunkscore, chunk))
    scores.sort(key = lambda x:x[0], reverse = True)
    return scores[:num_chunks]


def summarize(text, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{text}"}]
    )
    return response.choices[0].message.content

def getlanguage(file):
    text = load_text(file)
    chunk = chunk_text_by_words(text, 100)[0]
    response = summarize(chunk+"what language is the above text in - answer in one word")
    return response


def main():
    print("welcome to doc-chat!")
    file = input("enter file here: ")
    text = load_text(file)
    language = getlanguage(file)
    while True: 
        query = input("question or type 'q' to quit: ")
        if query == 'q':
            break
        importantchunks = find_relevant_chunks(text, query, 5)
        totalquery = ""
        for chunk in importantchunks:
            totalquery += chunk[1] + "\n"
        totalquery += query + " please answer in" + language 
        print(totalquery)
        response = summarize(totalquery)
        print(response)



main()