
responses = {
    "capital of france": "Paris",
    "capital of india": "New Delhi",
    "who created python": "Guido van Rossum"
}
question = input("Ask: ").lower()
answer = responses.get(question, "I don't know")
print(answer)

"""
LLMS basically predict the next token of a given query at a large
scale eg:chatgpt , claude ,gemini etc
Actual LLMs are doing:
Input
 ↓
Predict Next Token
 ↓
Generate Response

but at a much larger scale.
"""