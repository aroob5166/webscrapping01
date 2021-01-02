import requests
from bs4 import BeautifulSoup
url = "https://www.zomato.com/cincinnati/delhi-restaurants"
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
searchList = soup.find_all(
    'div' , {"class": "js-search-result-li "})

print(len(searchList))