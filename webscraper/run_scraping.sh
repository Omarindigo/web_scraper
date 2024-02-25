#!/bin/bash

# Prompt the user for a URL
read -p "Enter the URL to scrape: " URL

echo "Fetching HTML content from $URL"
python fetch_html.py "$URL"

echo "Parsing HTML to extract image URLs..."
python parse_html.py

echo "Downloading images..."
python download_images.py

echo "Scraping process completed!"
