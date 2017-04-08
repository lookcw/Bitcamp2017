import csv
import newspaper
from newspaper import Article


def get_article(url):
	a = Article(url, language='en')
	a.download()
	a.parse()
	return a.text.replace('\n', '')


def get_urls(col,input_file,output_file,delim,cate):
	url_file=open(input_file,'r')
	url_reader=csv.reader(url_file,delimiter=delim)
	headlines_file = open(output_file,'w')
	headlines_writer=csv.writer(headlines_file,delimiter=',')
	n=0
	for line in url_reader:
		print line[col]
		if n%30==0:
			try:	
				url = line[col]
				headlines_writer.writerow([url,cate])
			except:
				print "not found"
		n=(n+1)%30

get_urls(1,"url_data/real/newsCorpora.csv","newsCorpora_headlines.csv","\t","real")
#get_urls(1,"url_data/real/newsCorpora.csv","newsCorpora_headlines.txt","\t")
#get_urls(3,"url_data/real/2pageSessions.csv","2pageSessionsArticles.txt","\t")



	






