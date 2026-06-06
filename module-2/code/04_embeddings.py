#pip install sentence-transformers
from sentence_transformers import SentenceTransformer
# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
text = "Machine Learning"
embedding = model.encode(text)

print("Text:")
print(text)

print("\nEmbedding Shape:")
print(embedding.shape)

print("\nFirst 10 values:")
print(embedding[:10])
"""
------------------------------Output---------------------------
Text:
Machine Learning

Embedding Shape:
(384,)

First 10 values:
[-0.02439179  0.00324442  0.05426767 -0.00667262  0.00393569 -0.00795744
  0.02502521 -0.03203272 -0.05451072 -0.04470205]
--------------------------------------------------------------
A Sentence Transformer is a model that converts ,word/sentence/paragraph
into a Dense Vector (Embedding) that captures semantic meaning.

eg: 
model.encode("Machine Learning")
O/p
[-0.12, 0.45, 0.89, ...]
Uses: Semantic Search ,RAG,Agent memory,recommendation systems,document
retrieval etc.
Learn about sentence transformers here 👇
link : https://www.geeksforgeeks.org/nlp/sentence-transformer/
"""