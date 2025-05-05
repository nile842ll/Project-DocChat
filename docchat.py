from groq import Groq
from dotenv import load_dotenv
import os
import pdfplumber
from bs4 import BeautifulSoup
import argparse
import requests 
import sys
import simpleaudio as sa
"""
.venv/bin/python docchat.py
"""

load_dotenv()
client = Groq(api_key=os.getenv("GroqAPIKEY"))
print("Loaded API Key:", repr(os.getenv("GroqAPIKEY")))


def test_read_pdf_file(path):
    """
    Read PDFs
    >>> test_read_pdf_file("research_paper.pdf")[:20]
    'DOCSPLIT: Simple Con'

    """
    text = ''
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def test_read_file(path):
    """
    Read file
    >>> test_read_file("declaration2")[:20]
    'In Congress, July 4,'
    """
    with open(path, "r") as file:
        text = file.read()
    return text

def test_read_html_file(path):
    """
    Read from html file
    >>> test_read_html_file("dracula.html")[:20]
    'The Project Gutenber'

    """
    text = ''
    with open(path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
    return text

def read_website(url):
    """
    Gather text from website
    >>> read_website("http://NOTREALWERWRewrfdvdWERE.COM")
    failtoread http://NOTREALWERWRewrfdvdWERE.COM
    """
    try: 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text   
    except Exception as e:
        print("failtoread", url)



def load_text(filepath_or_url):
    """
    Loads text from a filepath or URL. Supports .txt, .html, .pdf, and online pages.

    >>> isinstance(load_text("dracula_chapter1.txt"), str)
    True
    """
    if ".pdf" in filepath_or_url:
        return test_read_pdf_file(filepath_or_url)
    if ".txt" in filepath_or_url:
        return test_read_file(filepath_or_url)
    if ".html" in filepath_or_url:
        return test_read_html_file(filepath_or_url)
    if "https" in filepath_or_url and not ".jpg" in filepath_or_url:
        return read_website(filepath_or_url)


def chunk_text_by_words(text, max_words=100, overlap=50):
    """
    Splits text into an amount of words
    >>> chunk_text_by_words("the cat sat on the mat", 3, 0)
    ['the cat sat', 'on the mat']
    """
    words = text.split()
    chunks = []
    for i in range(0,len(words), max_words-overlap):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

#this finds same overlapping words only , not synonyms 
def score_chunk(chunk, query):
    """
    Calculates overlap-based similarity between a text chunk and query.

    >>> score_chunk("the cat sat on the mat", "cat mat")
    0.3333333333333333
    """
    chunkwords = chunk.split()
    querywords = query.split()
    commonwords = set(chunkwords).intersection(set(querywords))
    similarity = len(commonwords)/max(len(chunkwords), len(querywords))
    return similarity


def find_relevant_chunks(text, query, num_chunks=5):
    """
    Returns the top N relevant text chunks given a query.

    >>> isinstance(find_relevant_chunks("cat dog fish", "dog", 1), list)
    True
    """
    chunks = chunk_text_by_words(text, 20, 10)
    scores = []
    for chunk in chunks:
        chunkscore = score_chunk(chunk, query)
        scores.append((chunkscore, chunk))
    scores.sort(key = lambda x:x[0], reverse = True)
    return scores[:num_chunks]


def summarize(text, model="llama-3.3-70b-versatile"):
    """
    Summarizes text using LLM 
    >>> summarize("say the word poem one time in lowercase")
    'poem'
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{text}"}]
    )
    return response.choices[0].message.content



def getlanguage(file):
    """
    Tells you language of file
    >>> getlanguage("constitution-mx.txt")
    'Spanish'

    """
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




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

