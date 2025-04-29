# DocChat: Talk to Your Documents with AI

DocChat is a Python-based command-line tool that allows users to interact with documents by asking natural language questions. Powered by large language models, it retrieves relevant document sections and provides insightful (and sometimes not-so-insightful) answers.

![Test Cases](https://github.com/nile842ll/Project-DocChat/actions/workflows/tests.yml/badge.svg)

## Demo

![Demo Gif](link-to-your-demo.gif)

## Installation

## Usage

python3 main.py --document_path example.txt

Then, simply type your question when prompted.

## Example

### Good answer:

> What is the main argument of this document?

The main argument of the document is that effective communication between humans and machines is becoming increasingly vital in modern society, as demonstrated by the growing use of AI tools.

### Poor answer:

> How does this document relate to quantum physics?

I'm not sure. It mentions "communication," but there are no direct references to quantum physics.

## Project Structure

main.py                     # Entry point for running the document chat program
requirements.txt            # Lists all dependencies
.github/workflows/tests.yml # Continuous integration setup to automatically run tests
tests/                      # Contains test cases to ensure program functionality

## Features

- Chat with any text document
- Simple command-line interface
- Robust error handling
- Automated testing with GitHub Actions


