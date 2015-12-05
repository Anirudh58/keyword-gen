from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p', attrs = {"itemprop" : "articleBody"}):
		articletext += tag.text

	return articletext

def getArticleTextTOI(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('div', attrs = {"class" : "Normal"}):
		articletext += tag.text

	return articletext

def getArticle(url):

        if "timesofindia" in url:
                htmltext = gethtml.getHtmlText(url)
                return getArticleTextTOI(htmltext)

        else:
                htmltext = gethtml.getHtmlText(url)
                return getArticleText(htmltext)

def getKeyword(articletext):
	word_dict = {}
	word_list = articletext.lower().split()

	common = open("common.txt").read().split('\n')

	


	for word in word_list:
		if word not in common and word.isalpha():
			if  word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1

	topword = sorted(word_dict.items(), key = lambda(k,v):(v,k), reverse = True)[0:25]
	top25=[]

	for each in topword:
		top25.append(each[0])

	return top25
