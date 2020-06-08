import csv
import re
key = {}

fichier = open('mbti_1.csv', 'r', encoding="utf8",)
fichiercsv = csv.reader(fichier, delimiter=',')
listecsv = []
isExist = 0
for ligne in fichiercsv:
    isExist = 0
    ligne[1] = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", ligne[1])
    ligne[1] = ligne[1].replace("||||||", "|||")
    ligne[1] = ligne[1].replace(",", " ")
    ligne[1] = ligne[1].replace('\"', "")
    ligne[1] = ligne[1].replace("\'", "")
    for lignecsv in listecsv:
        if lignecsv[0] == ligne[0]:
            isExist = 1
            lignecsv[1] = lignecsv[1] + '|||' + ligne[1]
            break
    if isExist == 0:
        listecsv.append(ligne)

out = open('mbti_1_edit.csv', "w", encoding="utf8",)
outw = csv.writer(out)
outw.writerows(listecsv)
out.close()
fichier.close()
