thonimport os
import json
from extractors.instagram_parser import parse_instagram_location
from outputs.exporters import export_to_json

def run_scraper(location_urls, max_items=1000, date_filter=None):
    results = []
    for url in location_urls:
        data = parse_instagram_location(url, max_items, date_filter)
        results.extend(data)
    export_to_json(results, 'output.json')

if __name__ == "__main__":
    location_urls = ['https://www.instagram.com/explore/locations/1/', 'https://www.instagram.com/explore/locations/2/']
    run_scraper(location_urls)