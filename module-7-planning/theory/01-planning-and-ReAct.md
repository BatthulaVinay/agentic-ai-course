# Module 4: Planning and Reasoning in Agents

## Introduction

In previous modules, we learned how agents use tools, retrieve information through RAG, and maintain memory. However, a truly intelligent agent needs more than memory and retrieval. It must be able to think through problems, break large goals into smaller tasks, decide what actions to take, and continuously evaluate its progress.

This capability is known as Planning and Reasoning.

---

# What is Planning?

Planning is the process of breaking a large objective into smaller executable tasks.

Instead of directly solving a complex problem, an agent first creates a roadmap of steps required to reach the goal.

### Example

Goal:

```text
Build an AI Startup
```

Possible Plan:

```text
Generate Idea
↓
Market Research
↓
Build MVP
↓
Testing
↓
Deployment
↓
Acquire Users
```

The sequence of actions forms the plan.

---

# What is Reasoning?

Reasoning is the process of deciding what to do next based on available information.

While planning answers:

```text
What steps should I take?
```

Reasoning answers:

```text
What should I do right now?
```

### Example

Question:

```text
Can I go outside?
```

Reasoning:

```text
Check Weather
↓
If raining → Take umbrella
Else → Go normally
```

The decision-making process is reasoning.

---

# Planning vs Reasoning

| Planning                | Reasoning                        |
| ----------------------- | -------------------------------- |
| Creates the roadmap     | Makes decisions during execution |
| Focuses on future steps | Focuses on the current step      |
| Breaks goals into tasks | Determines the next action       |
| Strategic               | Tactical                         |

---

# Evolution of AI Systems

## Traditional LLM

```text
Question
↓
Answer
```

The model directly generates a response.

---

## Tool Agent

```text
Question
↓
Choose Tool
↓
Execute Tool
↓
Answer
```

The model can now access external information.

---

## Planning Agent

```text
Question
↓
Create Plan
↓
Execute Steps
↓
Evaluate Progress
↓
Answer
```

The model can solve larger and more complex tasks.

---

# Chain of Thought (CoT)

Chain of Thought is a reasoning technique where the model explicitly generates intermediate reasoning steps before producing an answer.

Instead of:

```text
Solve this problem.
```

Use:

```text
Think step-by-step and solve this problem.
```

The model reasons before answering.

---

## Chain of Thought Workflow

```text
Problem
↓
Reasoning Step 1
↓
Reasoning Step 2
↓
Reasoning Step 3
↓
Answer
```

---

## Example

Question:

```text
15 workers complete work in 20 days.
How many days will 30 workers take?
```

Reasoning:

```text
15 × 20 = 300 worker-days

300 ÷ 30 = 10 days
```

Answer:

```text
10 days
```

---

# Limitation of Chain of Thought

Chain of Thought only performs reasoning.

It cannot:

* Use tools
* Search the internet
* Access databases
* Execute actions

This limitation led to the development of ReAct.

---

# ReAct Framework

ReAct stands for:

```text
Reason + Act
```

Instead of only thinking, the agent can:

1. Think
2. Take an action
3. Observe the result
4. Think again

---

# ReAct Cycle

```text
Thought
↓
Action
↓
Observation
↓
Thought
↓
Action
↓
Observation
↓
Final Answer
```

---

## Example

User:

```text
What is the weather in Trivandrum?
```

Thought:

```text
I need weather information.
```

Action:

```text
Call Weather Tool
```

Observation:

```text
31°C, Sunny
```

Thought:

```text
I have enough information.
```

Final Answer:

```text
The weather is 31°C and sunny.
```

---

# Why ReAct is Important

Without ReAct:

```text
Tool
↓
Answer
```

With ReAct:

```text
Think
↓
Choose Tool
↓
Observe Result
↓
Reason Again
↓
Answer
```

The agent becomes more reliable and intelligent.

---

# Agent Loop

Real-world agents rarely stop after one tool call.

Instead, they continuously:

```text
Think
↓
Act
↓
Observe
↓
Think Again
```

until the objective is achieved.

This repeating process is called an Agent Loop.

---

# Agent Loop Architecture

```text
Goal
↓
Thought
↓
Action
↓
Observation
↓
Enough Information?
│
├── No → Continue Loop
│
└── Yes → Final Answer
```

---

# Example: Internship Research Agent

User:

```text
Find AI internships and compare them.
```

Thought:

```text
Need internship information.
```

Action:

```text
Search internships.
```

Observation:

```text
3 internships found.
```

Thought:

```text
Need eligibility information.
```

Action:

```text
Open internship pages.
```

Observation:

```text
Eligibility collected.
```

Thought:

```text
Enough information available.
```

Final Answer:

```text
Comparison generated.
```

---

# Task Decomposition

Task decomposition is the process of breaking large goals into smaller manageable tasks.

Example:

```text
Build CNN Plant Disease Classifier
```

becomes:

```text
Collect Dataset
↓
Preprocess Images
↓
Train CNN
↓
Evaluate Model
↓
Deploy Application
```

Large problems become easier to solve.

---

# Reflection

Advanced agents evaluate their own work before returning an answer.

Workflow:

```text
Generated Answer
↓
Review Answer
↓
Improve Answer
↓
Final Answer
```

This process is called Reflection.

---

# Reflection Loop

```text
Answer
↓
Critic
↓
Issues Found?
│
├── Yes → Improve
│
└── No → Finish
```

---

## Example

Initial Answer:

```text
Python is used in AI.
```

Critic:

```text
Too generic.
```

Improved Answer:

```text
Python is widely used in AI because of libraries such as TensorFlow, PyTorch, and Scikit-Learn.
```

---

# Types of Planning

## Single-Step Planning

```text
Question
↓
Tool
↓
Answer
```

Suitable for simple tasks.

---

## Multi-Step Planning

```text
Question
↓
Plan
↓
Task 1
↓
Task 2
↓
Task 3
↓
Answer
```

Suitable for most agent systems.

---

## Dynamic Planning

The plan changes during execution.

Example:

```text
Search failed
↓
Create Alternative Plan
↓
Continue Execution
```

Used by advanced autonomous agents.

---

# Modern Agent Architecture

```text
User Goal
      │
      ▼

Planner
      │
      ▼

Task List
      │
      ▼

Agent Loop
      │
      ▼

Tools
      │
      ▼

Observations
      │
      ▼

Reflection
      │
      ▼

Final Answer
```

---

# Real Systems Using These Concepts

## Cursor

Uses:

* Planning
* Tool Usage
* Reflection
* File Operations

---

## Devin

Uses:

* Long-Term Planning
* Multi-Step Execution
* Self-Correction

---

## Claude Code

Uses:

* ReAct
* Tool Calling
* Reflection Loops

---

# Key Takeaways

* Planning breaks large goals into smaller tasks.
* Reasoning determines the next action.
* Chain of Thought improves problem solving through step-by-step reasoning.
* ReAct combines reasoning and tool usage.
* Agent Loops allow iterative problem solving.
* Task Decomposition simplifies complex objectives.
* Reflection improves answer quality before final output.
* Modern AI agents rely heavily on planning and reasoning to solve real-world problems autonomously.

---

# What We Learned Today

By the end of this lesson, you should understand:

✅ What Planning is

✅ What Reasoning is

✅ Difference between Planning and Reasoning

✅ Chain of Thought (CoT)

✅ ReAct Framework

✅ Agent Loops

✅ Task Decomposition

✅ Reflection Loops

✅ Types of Planning

✅ Modern Agent Architecture

✅ How systems like Cursor, Devin, and Claude Code operate internally

This forms the foundation for building autonomous agents capable of solving multi-step real-world tasks.

#

# &#x20;ReAct Agent Implementation

## Introduction

In the previous lesson, we learned the concepts of Planning, Reasoning, Chain of Thought (CoT), ReAct, Agent Loops, Task Decomposition, and Reflection.

However, all those concepts were theoretical.

In this lesson, we move towards implementation and understand how modern agents such as Cursor, Claude Code, Devin, and OpenAI Agents operate internally using the ReAct framework.

The goal is to understand how an agent can think, take actions, observe results, and continue reasoning until it reaches a solution.

---

# Why ReAct Exists

Consider the question:

```text
What is the weather in Trivandrum?
```

A traditional LLM works as:

```text
Question
↓
Answer
```

The model attempts to answer using only its internal knowledge.

This becomes problematic because:

* Knowledge may be outdated
* The model cannot access live information
* The model cannot verify facts

To solve this, tools were introduced.

---

# Tool-Based Agent

A tool-based agent works as:

```text
Question
↓
Choose Tool
↓
Execute Tool
↓
Answer
```

Example:

```text
User:
What is the weather in Trivandrum?

↓

Weather Tool

↓

31°C, Sunny

↓

Final Answer
```

This is already better than a traditional LLM.

However, it still has limitations.

The agent is simply calling a tool without reasoning deeply about what to do next.

---

# ReAct Framework

ReAct stands for:

```text
Reason + Act
```

The key idea is that an agent should alternate between:

```text
Thinking
Acting
Observing
```

instead of directly answering.

---

# Core ReAct Cycle

```text
Thought
↓
Action
↓
Observation
↓
Thought
↓
Action
↓
Observation
↓
Final Answer
```

This cycle allows the agent to reason while interacting with external tools.

---

# Understanding Each Component

## Thought

The Thought step represents reasoning.

The agent decides:

```text
What information do I need?
What should I do next?
```

Example:

```text
I need weather information.
```

---

## Action

The Action step represents tool execution.

Example:

```text
Call Weather Tool
```

The agent performs an operation to gather information.

---

## Observation

Observation is the result returned by the tool.

Example:

```text
31°C, Sunny
```

The agent now has new information.

---

## New Thought

The agent reasons again.

Example:

```text
I now have the required weather information.
```

---

## Final Answer

The agent produces a response using the information gathered during previous steps.

---

# ReAct Architecture

```text
User Query
      │
      ▼

Thought
      │
      ▼

Action
      │
      ▼

Tool Execution
      │
      ▼

Observation
      │
      ▼

Thought
      │
      ▼

Action
      │
      ▼

Observation
      │
      ▼

Final Answer
```

---

# Example Walkthrough

## User Query

```text
Find AI internships.
```

---

## Thought

```text
I need internship information.
```

---

## Action

```text
Search Internship Tool
```

---

## Observation

```text
3 internships found.
```

---

## Thought

```text
Need eligibility details.
```

---

## Action

```text
Open Internship Pages
```

---

## Observation

```text
Eligibility information collected.
```

---

## Thought

```text
I have enough information.
```

---

## Final Answer

```text
Comparison generated.
```

---

# Simple ReAct Agent Implementation

```python
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
```

---

# Understanding the Code

When the user enters:

```text
Find AI internships
```

the execution flow becomes:

```text
THOUGHT
↓
Understand user request

ACTION
↓
Call Internship Tool

OBSERVATION
↓
Internship List Returned

THOUGHT
↓
Enough information available

FINAL ANSWER
```

This is the first practical implementation of the ReAct cycle.

---

# Why This Is Not Yet a True Agent

Notice:

```python
if "weather" in query:
```

and

```python
if "internship" in query:
```

are hardcoded.

This means:

* Tool selection is manually programmed
* The agent cannot generalize
* New tools require modifying the code

This is not scalable.

---

# Real ReAct Agents

Modern agents use an LLM to generate the Thought step.

Instead of:

```python
if "weather" in query:
```

the workflow becomes:

```text
User Query
↓
LLM Generates Thought
↓
Tool Selection
↓
Tool Execution
↓
Observation
↓
LLM Generates Next Thought
↓
Next Action
```

This creates a much more autonomous system.

---

# Agent Loop

A real agent rarely stops after one action.

Instead, it repeatedly executes:

```text
Thought
↓
Action
↓
Observation
↓
Thought
↓
Action
↓
Observation
```

until the goal is achieved.

This repeating process is called an Agent Loop.

---

# Agent Loop Architecture

```text
Goal
 ↓

Thought
 ↓

Action
 ↓

Observation
 ↓

Goal Completed?

 No
  │
  ▼

Thought Again

 Yes
  │
  ▼

Final Answer
```

---

# ReAct vs Chain of Thought

## Chain of Thought

```text
Think
↓
Think
↓
Think
↓
Answer
```

Characteristics:

* Internal reasoning only
* No tool usage
* No external interaction

---

## ReAct

```text
Think
↓
Tool
↓
Observe

Think
↓
Tool
↓
Observe

Answer
```

Characteristics:

* Uses tools
* Interacts with external systems
* Dynamic reasoning

---

# Why Cursor Feels Intelligent

Cursor internally performs:

```text
Thought
↓
Read File
↓
Observation
↓
Thought
↓
Edit File
↓
Observation
↓
Thought
↓
Run Terminal
↓
Observation
```

This is essentially an advanced ReAct loop.

---

# Why Devin Feels Autonomous

Devin performs:

```text
Planning
↓
ReAct Loop
↓
Reflection
↓
ReAct Loop
↓
Final Solution
```

The repeated cycles make the system appear autonomous.

---

# Interview Questions

### What does ReAct stand for?

```text
Reason + Act
```

---

### What are the three core components of ReAct?

```text
Thought
Action
Observation
```

---

### What is the purpose of Observation?

Observation provides feedback from tool execution so the agent can make better decisions.

---

### Why is ReAct better than Chain of Thought?

Because ReAct can interact with tools and external environments.

---

### What is an Agent Loop?

A repeated cycle of:

```text
Thought
↓
Action
↓
Observation
↓
Repeat
```

until the objective is achieved.

---

# Key Takeaways

* ReAct stands for Reason + Act.
* ReAct combines reasoning with tool usage.
* The core cycle is Thought → Action → Observation.
* Agent Loops repeatedly execute the ReAct cycle until a goal is completed.
* Modern AI agents such as Cursor, Claude Code, and Devin are built on advanced versions of ReAct.
* ReAct is the foundation of autonomous agent behavior.

---

# What We Learned Today

By the end of this lesson, you should understand:

✅ Why ReAct exists

✅ Difference between Tool Agents and ReAct Agents

✅ Thought → Action → Observation cycle

✅ Agent Loops

✅ Practical ReAct implementation

✅ ReAct vs Chain of Thought

✅ How Cursor and Devin use ReAct internally

✅ Why modern Agentic AI systems rely on iterative reasoning and tool usage
