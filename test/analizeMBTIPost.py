from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import csv
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

fichier = open('mbti_1_edit.csv', 'r', encoding="utf8", )
for ligneS in fichier:
	wordsFiltered = []
	stopWords = set(stopwords.words('english'))
	ligne = ligneS.split(',')
	if len(ligne) > 1:
		ligne[1] = ligne[1].replace("|||", " ")
		ligne[1] = ligne[1].lower()
		words = tokenizer.tokenize(ligne[1])
		for w in words:
			if w not in stopWords:
				wordsFiltered.append(w)
	countWordOccurence = Counter(wordsFiltered)
	print(countWordOccurence)
fichier.close()