## Tokens
In this module , we gonna discuss about tokens as well as embeddings
Tokens are a chunk of text,understand tokens and words are not the same ,in llms we tokenize the words and sentences
Example:
Hello World
May become:
["Hello", "World"]

But:
unbelievable
might become:
["un", "believ", "able"] :This is called subword tokenization.

And:
ChatGPT
might become:
["Chat", "G", "PT"]

Models use subword tokenization because they learn patterns better than the indiviual words.
Understand:The model never sees the sentence directly.It only sees tokens.
 ![alt text](image.png)

---
## Token ids and Embeddings

Computers cannot understand tokens so these are converted to numbers known as the token ids.
So basically computers see the token ids! These ids are like identifications of tokens.
These token ids are n't enough for overseeing the similarity between tokens.So we need something more...
Token ids:
     cat = 51
     dog = 84
---

Embeddings are vector representation of tokens which also oversees their semantic meaning
The words similar to each other will be closer and different words would be farther

Cat
might become:
[0.2, 0.8, 0.1, 0.7]

Dog:
[0.3, 0.7, 0.2, 0.8]

Car:
[0.9, 0.1, 0.8, 0.2]

Notice:
Cat ≈ Dog
Vectors are similar.
Thus, embeddings are numerical representations of meaning.

![alt text](image-1.png)
![alt text](image-2.png)

---

## Context Window
Context Window = Working Memory.
From the meaning , we can say that it is memory of the current context (current chat)

Imagine I tell you:
My name is Mekha.

Then 2 minutes later:

What's my name?
Why can ChatGPT answer?

Because both messages fit inside its context window.
 Token 1
 Token 2
 Token 3
  ...
 Token 128000
 The model can see all of them simultaneously.
 Note : This is NOT long-term memory.It's only,current conversation memory.



