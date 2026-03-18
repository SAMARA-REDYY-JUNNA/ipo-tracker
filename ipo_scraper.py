import requests
from bs4 import BeautifulSoup

def get_ipos():
    url = "https://www.chittorgarh.com/ipo/ipo_list.asp"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "table"})

    ipo_list = []

    if table:
        rows = table.find_all("tr")[1:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 0:
                ipo = {
                    "name": cols[0].text.strip(),
                    "open_date": cols[1].text.strip(),
                    "close_date": cols[2].text.strip(),
                    "price": cols[4].text.strip()
                }
                ipo_list.append(ipo)

    return ipo_list