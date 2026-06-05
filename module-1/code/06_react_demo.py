def weather_tool():
    return "31°C"

print("Question: Weather in Kerala?")

print("\nThought:")
print("Need weather information")

print("\nAction:")
print("Calling weather_tool()")

result = weather_tool()

print("\nObservation:")
print(result)

print("\nFinal Answer:")
print(f"Current weather is {result}")

"""
Question: Weather in Kerala?

Thought:
Need weather information

Action:
Calling weather_tool()

Observation:
31°C

Final Answer:
Current weather is 31°C
"""