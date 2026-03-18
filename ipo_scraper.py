import requests
from bs4 import BeautifulSoup

def get_ipos():
    url = "https://www.chittorgarh.com/ipo/ipo_list.asp"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ipo_list = []

    tables = soup.find_all("table")

    for table in tables:
        rows = table.find_all("tr")

        for row in rows[1:]:
            cols = row.find_all("td")

            if len(cols) >= 5:
                ipo = {
                    "name": cols[0].text.strip(),
                    "open_date": cols[1].text.strip(),
                    "close_date": cols[2].text.strip(),
                    "price": cols[4].text.strip()
                }
                ipo_list.append(ipo)

    return ipo_list