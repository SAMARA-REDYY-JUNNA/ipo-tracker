import requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/ipo/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print("\nUpcoming IPO Details\n")

articles = soup.find_all("div")

count = 0

for item in articles:
    text = item.get_text(strip=True)

    if "IPO opens for subscription" in text:

        print("-----------------------------")
        print(text)
        print("-----------------------------\n")

        count += 1

    if count == 5:
        break