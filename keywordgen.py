import gethtml
import articletext

"""Feed nytimes/toi article url here"""

url = "http://timesofindia.indiatimes.com/world/us/How-the-Pakistani-entered-the-American-Homeland/articleshow/50050873.cms" 

text = articletext.getArticle(url)

print articletext.getKeyword(text)
