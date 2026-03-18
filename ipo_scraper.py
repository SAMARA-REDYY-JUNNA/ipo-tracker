from apify_client import ApifyClient
import pandas as pd

# Your Apify API token (get from Apify dashboard)
APIFY_TOKEN = "apify_api_XXXXX"
client = ApifyClient(APIFY_TOKEN)

# Run the IPO Calendar Scraper actor
run = client.actor("tropical_quince/ipo-calendar-scraper").call()

# Fetch dataset results
items = [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]

# Convert to DataFrame for easier inspection or export
df = pd.DataFrame(items)
open_ipos = df[df['status'].str.contains("Open", case=False, na=False)]
open_ipos.to_excel("Open_IPOs.xlsx", index=False)
print(f"IPO data saved — {len(open_ipos)} open IPO(s) found.")
