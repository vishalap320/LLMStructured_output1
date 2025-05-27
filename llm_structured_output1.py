from langchain_groq import ChatGroq
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  
os.environ["GROQ_API_KEY"] = ""


class Person(BaseModel):
    name: str = Field(description="Full name of the individual")
    age: int = Field(description="Age in years")
    address: str = Field(description="Residential address")
parser = PydanticOutputParser(pydantic_object=Person)

chat_model = ChatGroq(model="llama3-70b-8192", temperature=0)


input_text = "John Doe is 30 years old and lives at 123 Main St, Springfield."


format_instructions = parser.get_format_instructions()
prompt_template = PromptTemplate.from_template("""
Extract the following information from the text below:

{input_text}

{format_instructions}
""")

formatted_prompt = prompt_template.format(input_text=input_text, format_instructions=format_instructions)

response = chat_model.invoke(formatted_prompt)
response_content = response.content if isinstance(response.content, str) else str(response.content)
parsed_data = parser.parse(response_content)
print(parsed_data)