import requests

def get_ipos():
    url = "https://www.nseindia.com/api/ipo-current-issue"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/market-data/ipo",
        "Connection": "keep-alive"
    }

    try:
        session = requests.Session()

        # Step 1: Visit homepage (sets cookies)
        session.get("https://www.nseindia.com", headers=headers, timeout=5)

        # Step 2: Actual API call
        response = session.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            print("Failed to fetch data:", response.status_code)
            return []

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