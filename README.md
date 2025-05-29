#  LLM Structured Output Extractor with LangChain + Groq

This project demonstrates how to use **LangChain**, **Groq LLMs (LLaMA3)**, and **Pydantic** to extract structured data (like name, age, address) from natural language input.

---

## Demo

Given the input:

John Doe is 30 years old and lives at 123 Main St, Springfield.

The model returns:

```python
Person(name='John Doe', age=30, address='123 Main St, Springfield')
```
This is achieved by using a Groq-hosted LLM (LLaMA3) and parsing its output into a Pydantic model.

## Usage
This script is useful when:

You want structured JSON output from unstructured text using LLMs.

You need to extract key fields (like user profiles, product info, etc.) from raw sentences.

You are building an NLP pipeline that involves automated information extraction.

## How to Run This Code
1. Install dependencies:
 ```python
pip install langchain langchain-groq pydantic python-dotenv
```
2. Create a .env file:
```python
GROQ_API_KEY=your_actual_groq_key_here
```
3. Run the Python script:
```pyhton
python your_script_name.py
```
Run the Examples

You can replace the input text in this line:
```python
input_text = "John Doe is 30 years old and lives at 123 Main St, Springfield."
```
Make sure to store your Groq API key securely in a .env file. 
## Testing
To test different sentences:

Change the input_text.

Re-run the script.

Compare the printed output to check if the fields (name, age, address) are correctly parsed.

## How It Works
Loads your Groq API key securely via python-dotenv.

Classifies the input text into "personal", "TextSummary", or "other" categories.

According to classification, uses Pydantic models to parse and validate structured output.

Prints the parsed output as a Python object.

## What Can This Code Do?
Parse structured entities (name, age, address) from any descriptive sentence.

Validate and format output using Pydantic.

Help developers convert raw text into clean, structured Python data types.




