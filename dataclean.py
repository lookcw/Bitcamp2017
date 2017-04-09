import csv

realtrain = open("newsCorpora_headlines.csv", "r")
faketrain = open("fake.csv", "r")
reader = csv.reader(realtrain, delimiter=",")
realtrainarr = list(reader)
tmp = []
for row in realtrainarr:
	tmp.append(row[0])
realtrainarr = tmp
tmp = []
reader = csv.reader(faketrain, delimiter=",")
faketrainarr = list(reader)
tmp = []
for row in faketrainarr:
	tmp.append(row[0])
faketrainarr = tmp

print(realtrainarr)
print(faketrainarr)


realfull = open("uci-news-aggregator.csv", "r")
fakefull = open("fake_full.csv", "r")

reader = csv.reader(realfull, delimiter=",")
realtestarr = list(reader)
tmp = []
for row in realtestarr:
	if row[1] not in realtrainarr:
		if "," in row[1]:
			tmp.append('"' + row[1] + '",real')
		else:
			tmp.append(row[1]+",real")
realtestarr = tmp

reader = csv.reader(fakefull, delimiter=",")
faketestarr = list(reader)
tmp = []
for row in faketestarr:
	if row[4] not in faketrainarr:
		if "," in row[4]:
			tmp.append('"' + row[4] + '",fake')
		else:
			tmp.append(row[4]+",fake")
faketestarr = tmp

print(realtestarr)


#realtest = open("newsCorpora_headlines_test.csv", "w")
#for row in realtestarr:
#	realtest.write(row + "\n")
#faketest = open("fake_test.csv", "w")
#for row in faketestarr:
#	faketest.write(row + "\n")

