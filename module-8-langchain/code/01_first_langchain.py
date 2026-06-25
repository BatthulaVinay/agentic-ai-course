from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key
load_dotenv()

# Create the LLM
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Create Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Build the chain
chain = prompt | llm

# Execute
response = chain.invoke({
    "topic": "Machine Learning"
})

print(response.content)