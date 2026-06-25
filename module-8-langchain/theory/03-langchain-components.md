# Module 5: Agent Frameworks

# Lesson 3: LangChain Core Components

---

# Introduction

In the previous lesson, we learned that LangChain is a framework composed of reusable building blocks.

Instead of writing one large AI application, LangChain encourages developers to assemble applications using independent components, where each component performs one specific responsibility.

This design follows one of the most important principles in software engineering:

> **Single Responsibility Principle**

Every LangChain component exists because it solves one particular engineering problem.

In this lesson, we will study these components at a high level. Later lessons will explore each one in detail with practical code.

---

# Complete LangChain Architecture

```text
                        User
                          │
                          ▼
                  Prompt Template
                          │
                          ▼
                     Chat Model
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
    Retriever          Tools             Memory
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
                    Output Parser
                          │
                          ▼
                     Final Response
```

Notice that every block has only one responsibility.

---

# 1. Models

## Purpose

Models are responsible for communicating with Large Language Models.

Without models, LangChain cannot generate text.

Examples:

* OpenAI GPT
* Claude
* Gemini
* Llama
* Mistral
* DeepSeek

Architecture:

```text
Prompt
   │
   ▼
Chat Model
   │
   ▼
LLM
   │
   ▼
Generated Response
```

Think of Models as the communication layer between your application and an LLM.

---

# 2. Prompt Templates

## Purpose

Prompt Templates generate prompts dynamically.

Instead of manually concatenating strings, variables can be inserted automatically.

Architecture:

```text
Variables
     │
     ▼
Prompt Template
     │
     ▼
Formatted Prompt
     │
     ▼
Chat Model
```

Example:

Instead of writing:

```python
f"Explain {topic}"
```

LangChain provides reusable prompt templates.

Advantages:

* Reusable
* Cleaner
* Easier maintenance

---

# 3. Output Parsers

## Purpose

LLMs generate plain text.

Applications often require structured outputs.

Output Parsers convert raw text into structured formats.

Examples:

* JSON
* Lists
* Dictionaries
* Pydantic Models

Architecture:

```text
LLM Output
     │
     ▼
Output Parser
     │
     ▼
Structured Output
```

Useful for APIs and automation.

---

# 4. Chains

## Purpose

A Chain connects multiple components together.

Instead of calling everything manually:

```text
Prompt

↓

Model

↓

Parser
```

a Chain executes them as one pipeline.

Architecture:

```text
Input
   │
   ▼
Prompt
   │
   ▼
Model
   │
   ▼
Parser
   │
   ▼
Output
```

---

# 5. Runnables (LCEL)

Modern LangChain uses **Runnable** objects.

Everything becomes executable using a common interface.

Architecture:

```text
Input

↓

Runnable

↓

Output
```

Multiple runnables can be connected using the `|` operator.

This forms the foundation of **LangChain Expression Language (LCEL)**.

---

# 6. Tools

## Purpose

Tools allow the LLM to interact with external systems.

Examples:

* Calculator
* Weather API
* SQL Database
* Search Engine
* Python Interpreter

Architecture:

```text
User Query
      │
      ▼
Agent
      │
      ▼
Tool Selection
      │
      ▼
Tool Execution
      │
      ▼
Observation
```

This is exactly what we learned during Tool Calling.

---

# 7. Retrievers

## Purpose

Retrievers fetch relevant information from external knowledge sources.

Commonly used in RAG applications.

Architecture:

```text
User Query
      │
      ▼
Embedding
      │
      ▼
Vector Store
      │
      ▼
Retriever
      │
      ▼
Relevant Documents
      │
      ▼
LLM
```

Retrievers do **not** generate answers.

They only fetch relevant context.

---

# 8. Memory

## Purpose

Memory allows applications to remember previous interactions.

Architecture:

```text
Conversation
      │
      ▼
Memory
      │
      ▼
LLM
```

Examples:

* Conversation History
* User Preferences
* Long-Term Memory
* Session Memory

Memory improves personalization.

---

# 9. Agents

## Purpose

Agents decide which tool should be used.

Unlike chains, agents make decisions dynamically.

Architecture:

```text
User Query
      │
      ▼
Agent
      │
      ▼
Reasoning
      │
      ▼
Tool Selection
      │
      ▼
Tool Execution
      │
      ▼
Observation
      │
      ▼
Final Response
```

Agents implement the ReAct loop:

```text
Thought

↓

Action

↓

Observation

↓

Thought

↓

Answer
```

---

# 10. Document Loaders

## Purpose

Document Loaders read external files.

Examples:

* PDF
* DOCX
* TXT
* CSV
* HTML

Architecture:

```text
PDF

↓

Document Loader

↓

LangChain Document
```

These documents are later processed by Text Splitters.

---

# 11. Text Splitters

## Purpose

Large documents cannot be embedded directly.

Text Splitters divide them into smaller chunks.

Architecture:

```text
Large Document

↓

Text Splitter

↓

Chunk 1

Chunk 2

Chunk 3
```

Each chunk is then embedded separately.

This is a critical step in RAG pipelines.

---

# How Everything Connects

A typical RAG application combines multiple LangChain components.

```text
User Question
       │
       ▼
Prompt Template
       │
       ▼
Retriever
       │
       ▼
Relevant Documents
       │
       ▼
Chat Model
       │
       ▼
Output Parser
       │
       ▼
Final Answer
```

---

# Another Example: AI Coding Assistant

```text
User
   │
   ▼
Prompt Template
   │
   ▼
Agent
   │
   ▼
Tool Selection
   │
   ▼
Python Tool
   │
   ▼
Observation
   │
   ▼
Chat Model
   │
   ▼
Response
```

---

# Summary Table

| Component        | Responsibility               |
| ---------------- | ---------------------------- |
| Models           | Communicate with LLMs        |
| Prompt Templates | Generate prompts             |
| Output Parsers   | Structure outputs            |
| Chains           | Connect components           |
| Runnables        | Standard execution interface |
| Tools            | External actions             |
| Retrievers       | Retrieve knowledge           |
| Memory           | Store context                |
| Agents           | Decide actions               |
| Document Loaders | Read files                   |
| Text Splitters   | Split large documents        |

---

# Best Practices

* Use Prompt Templates instead of manual string formatting.
* Keep prompts reusable.
* Use Output Parsers when structured responses are required.
* Use Retrievers only for retrieval, not reasoning.
* Use Memory only when conversation history is necessary.
* Use Agents only when dynamic decision-making is required.
* Keep each component independent.

---

# Key Takeaways

* LangChain applications are built from reusable components.
* Each component has a single responsibility.
* Models communicate with LLMs.
* Prompt Templates generate reusable prompts.
* Output Parsers structure responses.
* Chains connect operations.
* Tools perform external actions.
* Retrievers fetch knowledge.
* Memory stores context.
* Agents perform reasoning and tool selection.
* Document Loaders and Text Splitters prepare data for RAG.

---

# Next Lesson

Now that you understand the architecture of LangChain, we will stop discussing theory and start writing code.

In the next lesson, we will build our **first LangChain application**, understand project structure, install the required packages, initialize an LLM, create Prompt Templates, and execute our first runnable pipeline.
