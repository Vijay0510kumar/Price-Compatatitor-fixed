import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scrapers.universal_google import scrape_google_results

def get_prices(query, country, groq_api_key):
    return scrape_google_results(query, country, groq_api_key)