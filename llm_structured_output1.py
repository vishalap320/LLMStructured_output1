from langchain_groq import ChatGroq
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")
os.environ["GROQ_API_KEY"] = groq_api_key
print("GROQ_API_KEY loaded successfully!")

# Personal Info Schema
class PersonalInfo(BaseModel):
    name: str = Field(description="The full name of the person")
    age: str = Field(description="Age of the person")
    address: str = Field(description="Full address of the person")


class TextSummary(BaseModel):
    main_idea: str = Field(description="The core message or thesis of the input text")
    benefits: list[str] = Field(description="Advantages mentioned in the text")
    challenges: list[str] = Field(description="Challenges or issues highlighted")
    tools_mentioned: list[str] = Field(description="Technologies, platforms, or tools referred to")
    conclusion: str = Field(description="Summary or final thoughts of the input")
    simple_txt: str = Field(description="Simple version of the text")

# Setup chat model
chat_model = ChatGroq(model="llama3-70b-8192", temperature=0)

# Function to classify input type
def classify_input(input_text: str) -> str:
    classify_prompt = PromptTemplate.from_template(
        "Classify the input text into one of the categories: 'personal', 'TextSummary', or 'other'.\n\n"
        "Text:\n"
        "{input_text}\n\n"
        "Return only the category."
    )
    prompt = classify_prompt.format(input_text=input_text.strip())
    response = chat_model.invoke(prompt)
    return response.content.strip().lower()

# Main analysis function
def analyze_text(input_text: str):
    classification = classify_input(input_text)

    if "personal" in classification:
        parser = PydanticOutputParser(pydantic_object=PersonalInfo)
        format_instructions = parser.get_format_instructions()

        prompt_template = PromptTemplate.from_template(
            "Extract structured personal information from the following text:\n\n"
            "Text:\n"
            "\"\"\"{input_text}\"\"\"\n\n"
            "{format_instructions}"
        )
    else:
        parser = PydanticOutputParser(pydantic_object=EducationTechSummary)
        format_instructions = parser.get_format_instructions()

        prompt_template = PromptTemplate.from_template(
            "Analyze the following educational text and extract structured information:\n\n"
            "Text:\n"
            "\"\"\"{input_text}\"\"\"\n\n"
            "{format_instructions}"
        )

    formatted_prompt = prompt_template.format(
        input_text=input_text.strip(),
        format_instructions=format_instructions
    )

    response = chat_model.invoke(formatted_prompt)
    response_content = response.content if isinstance(response.content, str) else str(response.content)

    return parser.parse(response_content)

# Entry point
if __name__ == "__main__":
    input_text = input("Enter text: ")
    result = analyze_text(input_text)
    print(result)
