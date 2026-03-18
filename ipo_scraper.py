import requests

def get_ipos():
    url = "https://api.stockedge.com/Api/IPO/GetIPOCalendar"

    try:
        response = requests.get(url)
        data = response.json()

        ipo_list = []

        for item in data:
            ipo = {
                "name": item.get("companyName", ""),
                "open_date": item.get("openDate", ""),
                "close_date": item.get("closeDate", ""),
                "price": item.get("priceBand", "")
            }
            ipo_list.append(ipo)

        return ipo_list

    except Exception as e:
        print("Error fetching IPO data:", e)
        return []