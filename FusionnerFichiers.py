#!/usr/bin/env python3

with open('Data/labels.csv', 'r') as labels :
	labell = labels.readlines()
labels.close()


with open('Data/dataset.csv', 'r') as dataset :
	avis = dataset.readlines()
dataset.close()

datasetResult = "@RELATION avisFilms\n\n@ATTRIBUTE avis String\n@ATTRIBUTE classLabel {-1,1}\n\n@Data\n"

for i in range(0, len(avis)) :
	datasetResult += "'" + avis[i].replace("'", "\\"+"\'").replace('"', "").replace("\n", "").replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(";", "").replace(":", "").replace(":", "").replace("*", " ")+ "',"+labell[i]
	
with open('Avis_Et_Label.arff', 'w') as fichier :
	fichier.write(datasetResult)
fichier.close()