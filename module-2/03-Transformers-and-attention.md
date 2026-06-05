## Transformer
The transformer model changed ai world forever.
In 2017:Attention Is All You Need, introduced the Transformers.
Before RNN and LSTM were used.
The core idea of transformers is that to see all words at once instead seeing it one by one.

## Attention
Imagine reading:
I went to the bank to deposit money.
When the model sees: bank
It asks: Which words should I pay attention to?
Attention scores might be:
| Word    | Attention |
| ------- | --------- |
| deposit | 0.50      |
| money   | 0.40      |
| went    | 0.05      |
| I       | 0.05      |
Because:deposit + money ,it indicate a financial bank.







