import pandas as pd
from nltk.tokenize import RegexpTokenizer

# here we are going to process word tokenizing and append a new "Tokens" column to our dataset

df = pd.read_csv("training_4plots.csv")
plot_list = df["Plot"].tolist()  # list of plots

tokenizer = RegexpTokenizer(r'\w+')

texts_list = []  # store the plot texts
words_list = []  # store the tokens list

for x in range(len(plot_list)):
    texts_list.append(plot_list[x])

for t in texts_list:
    words_list.append(tokenizer.tokenize(str(t)))

# df.insert(2, "Tokens", words_list)

for w in words_list:
    print(w)

# books_tokenized = df.to_csv(r'D:\DANT\DataScience\DataScienceProject\test\4books_stopwords_removed_tokens.csv')
