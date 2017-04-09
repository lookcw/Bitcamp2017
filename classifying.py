import csv
import json
from easygui import msgbox
from watson_developer_cloud import NaturalLanguageClassifierV1

test = open("test_set.csv", "r")
testdata = list(csv.reader(test, delimiter=","))

total = 0
correct = 0

natural_language_classifier = NaturalLanguageClassifierV1(
  username='d526c7d7-d2d1-4a52-a559-be3a2d5acff0',
  password='RePBJDyHIoVP')

for headline in testdata:
	print(headline, "bitch")
	classes = natural_language_classifier.classify('90e7acx197-nlc-35660', str(headline[0]))
	print(classes['classes'][0]['class_name'])
	print(headline[1])
	if (classes['classes'][0]['class_name']) == headline[1]:
		correct += 1
	total += 1

accuracy = correct / total
print("Accuracy of classifier:", accuracy)

#print(json.dumps(classes, indent=2))