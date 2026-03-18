import pandas as pd

def save_to_excel(data):

    df = pd.DataFrame(data)

    df.to_excel("ipo_data.xlsx", index=False)

    print("Excel file updated")