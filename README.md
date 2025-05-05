# DocChat: Talk to Your Documents with AI

DocChat is a Python-based command-line tool that lets you interact with documents by asking natural language questions. It uses a large language model to retrieve relevant sections and generate helpful (and sometimes not-so-helpful) answers.

![Test Cases](https://github.com/nile842ll/Project-DocChat/actions/workflows/tests.yml/badge.svg)

## Demo

![Demo Gif](docs/demo.gif) <!-- Make sure this file is uploaded to your GitHub repo under docs/ -->

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 docchat.py path/to/your/document.txt
```

Then, simply type your question when prompted.

## Example

```text
$ python3 docchat.py docs/sample.txt
docchat> What is the main argument of this document?
The main argument of the document is that effective communication between humans and machines is becoming increasingly vital in modern society, as demonstrated by the growing use of AI tools.

docchat> How does this document relate to quantum physics?
I'm not sure. It mentions "communication," but there are no direct references to quantum physics.
```

## Project Structure

```text
docchat.py                    # Main program file and entry point  
requirements.txt              # Lists all Python dependencies  
.github/workflows/tests.yml  # GitHub Actions workflow for automated testing  
tests/                        # Contains test cases (optional)
```

## Features

- Supports PDF, TXT, HTML, and URLs as input
- Retrieves and ranks relevant document sections
- CLI-based interaction
- LLM-powered responses using the Groq API
- Automated testing via `doctest` and GitHub Actions
