import csv
import json
from watson_developer_cloud import NaturalLanguageClassifierV1

to_test=""
natural_language_classifier = NaturalLanguageClassifierV1(
  username='d526c7d7-d2d1-4a52-a559-be3a2d5acff0',
  password='RePBJDyHIoVP')


classes = natural_language_classifier.classify('90e7acx197-nlc-35660', to_test)
print(classes['classes'][0]['class_name'])