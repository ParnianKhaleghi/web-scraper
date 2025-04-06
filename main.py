from urllib.request import urlopen
from bs4 import BeautifulSoup
from config import get_web_url


html = urlopen(get_web_url())
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)