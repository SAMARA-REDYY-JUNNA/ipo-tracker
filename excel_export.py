import pandas as pd


def save_excel(data):

    df = pd.DataFrame(data)

    df.to_excel("data/ipo_data.xlsx", index=False)

    print("Excel file updated")