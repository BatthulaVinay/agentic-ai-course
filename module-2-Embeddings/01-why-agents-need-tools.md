# Tool Selection and Routing

## Introduction

An agent may have access to multiple tools.

Example:

```python
calculator_tool()
weather_tool()
search_tool()
```

The challenge is deciding which tool to use.

This process is called Tool Selection.

---

## Example

User:

```text
What is 25 × 50 ?
```

Agent:

```text
Use calculator_tool
```

---

User:

```text
Weather in Kochi?
```

Agent:

```text
Use weather_tool
```

---

## Tool Routing

Tool routing refers to directing a query to the correct tool.

Workflow:

```text
User Query
↓
Intent Detection
↓
Tool Selection
↓
Tool Execution
```

---

## Metadata

Tools are usually described with metadata.

Example:

```python
{
  "name": "calculator",
  "description": "Perform mathematical calculations."
}
```

The LLM reads the description and chooses the correct tool.

---

## Key Takeaways

- Agents often have multiple tools.
- Tool selection determines which tool to use.
- Routing directs tasks to the correct tool.

# Function Calling

## Introduction

Function Calling is the mechanism that allows an LLM to request execution of a tool.

Instead of directly answering, the model generates a structured tool request.

---

## Example

User:

```text
Calculate 25 × 16
```

Model Output:

```json
{
  "tool": "calculator",
  "arguments": {
    "expression": "25 * 16"
  }
}
```

The application executes the tool.

---

## Workflow

```text
User Query
↓
LLM
↓
Function Call
↓
Tool Execution
↓
Result
↓
LLM
↓
Final Answer
```

---

## Benefits

- Reliable tool usage
- Structured communication
- Easy integration with external systems

---

## Key Takeaways

- Function calling connects LLMs to tools.
- Tools are executed outside the model.
- Results are returned to the model.

# Structured Outputs

## Introduction

Agents need predictable outputs.

Instead of free-form text:

```text
I think this is probably a weather query.
```

We prefer:

```json
{
  "intent": "weather",
  "city": "Kochi"
}
```

---

## Benefits

- Easier parsing
- More reliable automation
- Better integration with applications

---

## Common Formats

### JSON

```json
{
  "intent": "search"
}
```

### Dictionary

```python
{
  "tool": "calculator"
}
```

### Pydantic Models

Used in production systems.Pydantic is a Python data validation library used to define structured schemas using classes. It ensures that data follows expected types and formats. In Agentic AI, Pydantic is commonly used for structured outputs, tool inputs, API requests, API responses, and agent communication. It improves reliability by validating data before it is processed.

---

## Example

User:

```text
Weather in Delhi
```

Output:

```json
{
  "intent": "weather",
  "tool": "weather_tool",
  "arguments": {
    "city": "Delhi"
  }
}
```

---

## Key Takeaways

- Structured outputs make agents reliable.
- JSON is the most common format.
- Function calling depends on structured outputs.