import csv
import json
import pymsgbox
from watson_developer_cloud import NaturalLanguageClassifierV1

pymsgbox.alert('Welcome to Faux News', 'Title')
headline = pymsgbox.prompt('Enter a headline')

natural_language_classifier = NaturalLanguageClassifierV1(
  username='d526c7d7-d2d1-4a52-a559-be3a2d5acff0',
  password='RePBJDyHIoVP')

classes = natural_language_classifier.classify('90e7acx197-nlc-35660', headline)
pymsgbox.alert(classes['classes'][0]['class_name'], 'This news is...')
#print(classes)