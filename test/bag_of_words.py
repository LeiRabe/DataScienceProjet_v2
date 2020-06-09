import pandas as pd

# output_file = open('output_file.txt','w')
df = pd.read_csv('mettre_csv_ici.csv')
token_list = df["Tokens"].tolist()

bag_of_words = {}
bag_of_words_list = []

for word in token_list:
    # print(word)
    if word not in bag_of_words.keys():
        bag_of_words[word] = 1
    else:
        bag_of_words[word] += 1

for w in bag_of_words:
    print(w)
# output_file.close()
