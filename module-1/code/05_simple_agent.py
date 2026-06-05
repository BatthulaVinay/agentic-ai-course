def weather_tool():
    return "31°C"

def internship_tool():
    return "Found 10 ML internships"

query = input("Enter Query: ").lower()

print("\nTHOUGHT:")

if "weather" in query:

    print("Need weather information")

    print("\nACTION:")
    result = weather_tool()

elif "internship" in query:

    print("Need internship information")

    print("\nACTION:")
    result = internship_tool()

else:

    result = "Direct Answer"

print(result)

"""
Enter Query:
find internships

THOUGHT:
Need internship information
ACTION:
Found 10 ML internships

"""