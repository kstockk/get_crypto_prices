#!/usr/bin/env python
import sys
from datetime import datetime
from cryptocmd import CmcScraper

def main(coins):
    today = datetime.today().strftime('%d-%m-%Y')

    for coin in coins:
        scraper = CmcScraper(coin, "01-01-2022", today, False, True, "AUD")
        scraper.export("csv")

if __name__ == "__main__":
    main(sys.argv[1:])
