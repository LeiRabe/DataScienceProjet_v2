from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

df = pd.read_csv("book_tokenized_chunk1.csv")
stop_words = set(stopwords.words('english'))
print(df["Tokens"])
df["Tokens"] = df.Tokens.str.replace("[^\w\s]", "").str.lower()
df["Tokens"] = df["Tokens"].apply(lambda x: ' '.join([item for item in str(x).split() if item not in stop_words]))

clean_token_list = df["Tokens"].tolist()
clean_token_string_list = []

for w in clean_token_list:
    clean_token_string_list.append(word_tokenize(str(w)))

# for s in clean_token_string_list:
#  print(s)

df["Tokens"] = clean_token_string_list

print("//////////////////")
print(df["Tokens"])
books_tokenized = df.to_csv(r'D:\DANT\DataScience\DataScienceProject\test\book_tokenized_chunk1.csv')

