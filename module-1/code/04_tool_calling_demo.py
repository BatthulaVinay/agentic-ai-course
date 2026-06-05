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
In our Day 1 code, the weather value was hardcoded only for learning.
In a real agent, the weather tool retrieves live data from an API.
The real intelligence is not the API call itself, but the agent deciding that it needs to call 
the API to achieve the user's goal.(Observe-think-plan-act-observe)
"""