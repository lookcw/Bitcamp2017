import csv
import newspaper
from newspaper import Article
import sys

csv.field_size_limit(sys.maxsize)



def get_article(url):
	a = Article(url, language='en')
	a.download()
	a.parseset	
	return a.text.replace('\n', '')


def get_urls(col,input_file,output_file,delim,cate):
	url_file=open(input_file,'r')
	url_reader=csv.reader(url_file,delimiter=delim)
	headlines_file = open(output_file,'w')
	headlines_writer=csv.writer(headlines_file,delimiter=',')
	n=0
	for line in url_reader:
		print line[col]
		if n%60==1:
			try:
				url = line[col].replace(',',' ')
				if url:
					headlines_writer.writerow([url,cate])
			except:
				print "not found"
		n=(n+1)%60
get_urls(1,"url_data/real/newsCorpora.csv","test_newsCorpora_headlines.csv","\t","real")
#get_urls(1,"url_data/real/newsCorpora.csv","newsCorpora_headlines.txt","\t")
#get_urls(4,"url_data/fake/fake.csv","fake_test_set_headlines.csv",",","fake")
set


	






