import requests

def get_ipos():
    url = "https://www.nseindia.com/api/ipo-current-issue"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)  # 👈 important

        response = session.get(url, headers=headers)
        data = response.json()

        ipo_list = []

        for item in data.get("data", []):
            ipo = {
                "name": item.get("companyName", ""),
                "open_date": item.get("openDate", ""),
                "close_date": item.get("closeDate", ""),
                "price": item.get("priceBand", "")
            }
            ipo_list.append(ipo)

        return ipo_list

    except Exception as e:
        print("Error:", e)
        return []