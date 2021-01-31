
import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.python.org/"

resposta = urllib.request.urlopen(url)

bs = BeautifulSoup(resposta, 'html.parser')

print(str(resposta.info()))

listaDeLinks = bs.find_all('a')

for link in listaDeLinks:
    if link.has_attr('href') and re.search('http', link['href'] or re.search('https', link['href'])):
        print(link.prettify())












