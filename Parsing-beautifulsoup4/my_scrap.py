import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
      "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"}
list_card_url = []
for count in range(1,2):
    sleep(1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")
    for i in data:
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
        list_card_url.append(card_url)

for card_url in list_card_url:
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_ = "card mt-4 my-4")
    name = data.find("h3", class_ = "card-title")
    price = data.find("h4").text
    text = data.find("p", class_ = "card-text").text
    url_img = "https://scrapingclub.com" + data.find("img", class_ = "card-img-top img-fluid").get("src")
    
    print(data)

print(" ")