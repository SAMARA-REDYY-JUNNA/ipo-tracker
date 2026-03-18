import requests
from bs4 import BeautifulSoup

def get_ipos():
    url = "https://www.chittorgarh.com/report/ipo-calendar/82/"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        ipo_list = []

        table = soup.find("table")

        if not table:
            print("Table not found")
            return []

        rows = table.find_all("tr")

        for row in rows[1:]:
            cols = row.find_all("td")

            if len(cols) >= 6:
                ipo = {
                    "name": cols[0].text.strip(),
                    "open_date": cols[1].text.strip(),
                    "close_date": cols[2].text.strip(),
                    "price": cols[3].text.strip()
                }
                ipo_list.append(ipo)

        return ipo_list

    except Exception as e:
        print("Error:", e)
        return []