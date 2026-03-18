import requests

def get_ipos():
    url = "https://www.nseindia.com/api/ipo-current-issue"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/"
    }

    try:
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)

        response = session.get(url, headers=headers)

        if response.status_code != 200:
            print("Failed:", response.status_code)
            return []

        data = response.json()

        ipo_list = []

        # ✅ CORRECT LOOP POSITION
        if isinstance(data, list):
            for item in data:
                ipo = {
                    "name": item.get("companyName") or item.get("symbol", ""),
                    "open_date": item.get("openDate") or item.get("issueStartDate", ""),
                    "close_date": item.get("closeDate") or item.get("issueEndDate", ""),
                    "price": item.get("priceBand") or item.get("faceValue", "")
                }
                ipo_list.append(ipo)

        return ipo_list

    except Exception as e:
        print("Error:", e)
        return []