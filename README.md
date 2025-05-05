# DocChat: Talk to Your Documents with AI

DocChat is a Python-based command-line tool that allows users to interact with documents by asking natural language questions. Powered by large language models, it retrieves relevant document sections and provides insightful (and sometimes not-so-insightful) answers.

![Test Cases](https://github.com/nile842ll/Project-DocChat/actions/workflows/tests.yml/badge.svg)

## Demo

> ⚠️ Replace this broken link with a GIF uploaded directly to your GitHub repo and linked like this:
> `![Demo](demo.gif)` after uploading `demo.gif` to the repo root

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py --document_path example.txt
```

Then, simply type your question when prompted.

## Example

```
$ python3 docchat.py docs/sample.txt
docchat> What is the main argument of this document?
The main argument of the document is that effective communication between humans and machines is becoming increasingly vital in modern society, as demonstrated by the growing use of AI tools.

docchat> How does this document relate to quantum physics?
I'm not sure. It mentions "communication," but there are no direct references to quantum physics.
```


## Project Structure

```text
docchat.py                  # Main program file and entry point
requirements.txt            # Lists all Python dependencies
.github/workflows/tests.yml # GitHub Actions workflow for automated testing
tests/                      # Contains test cases (optional)
```

## Features

- Supports PDF, TXT, HTML, and URLs as input
- Retrieves and ranks relevant document sections
- CLI-based interaction
- LLM-powered responses using the Groq API
- Automated testing via `doctest` and GitHub Actions
