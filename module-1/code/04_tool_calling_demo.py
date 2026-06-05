def weather_tool():
    return "31°C"

query = input("Ask something: ")

if "weather" in query.lower():

    print("Using Weather Tool...")

    result = weather_tool()

    print(result)

else:
    print("No tool required.")

"""
The system:
               User Query
                   ↓
               Reason
                   ↓
               Select Tool
                   ↓
               Execute Tool
                   ↓
               Return Result

This is the beginning of Agentic AI, agentic systems use tools and memory in addition
to llms.
"""