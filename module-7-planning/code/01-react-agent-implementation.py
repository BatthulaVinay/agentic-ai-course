#a very simple code to understand how ReAct works
def weather_tool():
    return "31°C, Sunny"


def internship_tool():
    return [
        "AI Internship A",
        "ML Internship B",
        "Data Science Internship C"
    ]


def react_agent(query):

    print("\nTHOUGHT:")
    print("Understand the user request.")

    if "weather" in query.lower():

        print("\nACTION:")
        print("Call Weather Tool")

        observation = weather_tool()

        print("\nOBSERVATION:")
        print(observation)

        print("\nTHOUGHT:")
        print("I have weather information.")

        return observation

    elif "internship" in query.lower():

        print("\nACTION:")
        print("Call Internship Tool")

        observation = internship_tool()

        print("\nOBSERVATION:")
        print(observation)

        print("\nTHOUGHT:")
        print("I have internship information.")

        return observation

    else:

        return "No suitable action."


query = input("Ask Agent: ")

answer = react_agent(query)

print("\nFINAL ANSWER:")
print(answer)