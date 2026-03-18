import requests

def get_ipos():
    url = "https://api.stockedge.com/Api/IPO/GetIPOCalendar"

    try:
        response = requests.get(url)

        # Debug print
        print("RAW RESPONSE:", response.text[:200])

        data = response.json()

        ipo_list = []

        # Ensure data is list
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    ipo = {
                        "name": item.get("companyName", ""),
                        "open_date": item.get("openDate", ""),
                        "close_date": item.get("closeDate", ""),
                        "price": item.get("priceBand", "")
                    }
                    ipo_list.append(ipo)
        else:
            print("Unexpected data format:", type(data))

        return ipo_list

    except Exception as e:
        print("Error fetching IPO data:", e)
        return []