from ipo_scraper import get_ipos
from excel_writer import save_to_excel
from telegram_alert import send_alert


def load_history():
    try:
        with open("history.txt", "r") as f:
            return f.read().splitlines()
    except:
        return []


def save_history(ipo_name):
    with open("history.txt", "a") as f:
        f.write(ipo_name + "\n")


def run():

    data = get_ipos()
    print(data)
    history = load_history()

    new_ipos = []

    for ipo in data:
        if ipo["name"] not in history:
            new_ipos.append(ipo)
            save_history(ipo["name"])

    save_to_excel(data)

    if not new_ipos:
        print("No new IPO found")
        return

    message = "🚨 NEW IPO ALERT\n\n"

    for ipo in new_ipos:
        message += f"{ipo['name']}\n"
        message += f"Open: {ipo['open_date']}\n"
        message += f"Close: {ipo['close_date']}\n"
        message += f"Price: {ipo['price']}\n\n"

    send_alert(message)

    print("New IPO alert sent")


if __name__ == "__main__":
    run()