#  LLM Structured Output Extractor with LangChain + Groq

This project demonstrates how to use **LangChain**, **Groq LLMs (LLaMA3)**, and **Pydantic** to extract structured data (like name, age, address) from natural language input.

---

## Demo

Given the input:

John Doe is 30 years old and lives at 123 Main St, Springfield.

The model returns:

```python
Person(name='John Doe', age=30, address='123 Main St, Springfield')

This is achieved by using a Groq-hosted LLM (LLaMA3) and parsing its output into a Pydantic model.
```
##Usage
This script is useful when:

You want structured JSON output from unstructured text using LLMs.

You need to extract key fields (like user profiles, product info, etc.) from raw sentences.

You are building an NLP pipeline that involves automated information extraction.



