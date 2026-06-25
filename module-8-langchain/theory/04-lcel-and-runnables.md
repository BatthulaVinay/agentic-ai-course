# Module 5: Agent Frameworks

# Lesson 5: LangChain Expression Language (LCEL) & Runnables

---

# Introduction

In the previous lesson, we built our first LangChain application using a Prompt Template and a Chat Model. One line of code stood out:

```python
chain = prompt | llm
```

At first glance, this may look like a simple pipe operator. However, it is actually one of the most powerful features in modern LangChain.

This syntax is part of the **LangChain Expression Language (LCEL)**.

LCEL is a declarative way of connecting different LangChain components together to form an execution pipeline. Instead of manually calling each component one after another, LCEL allows developers to compose reusable pipelines that automatically pass data from one component to the next.

Understanding LCEL is essential because almost every modern LangChain project uses it.

---

# What is LCEL?

LCEL stands for **LangChain Expression Language**.

It is a language for describing how different LangChain components should work together.

Think of LCEL as a way of connecting LEGO blocks.

Each block performs one task.

When connected together, they become a complete AI application.

---

# Why Was LCEL Introduced?

Earlier versions of LangChain relied on classes such as:

* LLMChain
* SequentialChain
* SimpleSequentialChain

Although functional, these APIs became difficult to maintain and extend.

Modern AI applications require:

* Better readability
* Easy composition
* Parallel execution
* Streaming support
* Reusable pipelines

LCEL was introduced to solve these challenges.

---

# What is a Runnable?

A **Runnable** is the fundamental execution unit in LangChain.

A Runnable is simply an object that accepts an input and produces an output.

Mathematically:

```text
Input
   │
   ▼
Runnable
   │
   ▼
Output
```

Every major LangChain component is a Runnable.

Examples include:

* Prompt Templates
* Chat Models
* Output Parsers
* Retrievers
* Tools
* Chains

Because they all implement the same interface, they can easily be connected together.

---

# The Pipe Operator (`|`)

The pipe operator is the heart of LCEL.

It connects the output of one Runnable to the input of another Runnable.

Example:

```python
chain = prompt | llm
```

Execution flow:

```text
User Input
      │
      ▼
Prompt Template
      │
      ▼
Formatted Prompt
      │
      ▼
Chat Model
      │
      ▼
AIMessage
```

The output of the Prompt Template automatically becomes the input of the Chat Model.

---

# Chaining Multiple Components

LCEL allows multiple Runnables to be connected.

```python
chain = prompt | llm | parser
```

Execution flow:

```text
Input
   │
   ▼
Prompt Template
   │
   ▼
Chat Model
   │
   ▼
Output Parser
   │
   ▼
Final Output
```

Each component performs one responsibility and passes its output to the next.

---

# Advantages of LCEL

Compared to older Chain APIs, LCEL provides:

* Cleaner syntax
* Better readability
* Easy composition
* Reusable pipelines
* Parallel execution
* Streaming support
* Consistent execution model

This makes applications easier to build and maintain.

---

# Common Runnable Methods

Every Runnable supports a common set of methods.

### `invoke()`

Executes the pipeline for a single input.

```python
response = chain.invoke({"topic": "Machine Learning"})
```

---

### `batch()`

Executes the pipeline for multiple inputs.

```python
responses = chain.batch([
    {"topic": "AI"},
    {"topic": "Python"},
    {"topic": "RAG"}
])
```

Useful when processing many requests at once.

---

### `stream()`

Returns the response token by token instead of waiting for the complete output.

Useful for chat applications where users expect real-time responses.

---

### `ainvoke()`

Asynchronous version of `invoke()`.

Useful when building scalable web applications.

---

# Data Flow in LCEL

The data moves sequentially through the pipeline.

```text
Input

↓

Prompt Template

↓

Formatted Prompt

↓

Chat Model

↓

AIMessage

↓

Output Parser

↓

Structured Output
```

The developer does not manually move the data.

LCEL automatically handles the flow.

---

# Why LCEL is Important

Without LCEL:

```python
formatted_prompt = prompt.invoke(data)

response = llm.invoke(formatted_prompt)

result = parser.invoke(response)
```

With LCEL:

```python
chain = prompt | llm | parser

result = chain.invoke(data)
```

The logic remains the same, but the code becomes much cleaner and easier to understand.

---

# Best Practices

* Build applications using small Runnables.
* Keep each Runnable focused on one task.
* Use the pipe operator to compose pipelines.
* Prefer LCEL over legacy Chain classes.
* Reuse pipelines whenever possible.

---

# Interview Questions

### What is LCEL?

LCEL (LangChain Expression Language) is a declarative syntax for composing LangChain components into executable pipelines.

---

### What is a Runnable?

A Runnable is an object that accepts an input and produces an output. It is the fundamental execution unit in LangChain.

---

### What does the `|` operator do?

It connects the output of one Runnable to the input of another Runnable, forming a pipeline.

---

### Why is LCEL preferred over older Chain APIs?

Because it is more readable, composable, reusable, and supports advanced features such as streaming and parallel execution.

---

# Key Takeaways

* LCEL is the modern execution model of LangChain.
* Runnables are the basic execution units.
* The pipe operator (`|`) connects Runnables.
* `invoke()` executes a pipeline for one input.
* `batch()` processes multiple inputs.
* `stream()` returns incremental outputs.
* Modern LangChain development revolves around LCEL rather than legacy Chain classes.

---

# What We Learned Today

By the end of this lesson, you should understand:

✅ What LCEL is

✅ What a Runnable is

✅ Why LCEL replaced older Chain APIs

✅ How the pipe operator works

✅ Common Runnable methods

✅ How data flows through a LangChain pipeline

This knowledge forms the execution foundation for every modern LangChain application.
