import requests
from bs4 import BeautifulSoup
import pandas as pd

def download_html(url):
    """Download HTML content from the given URL."""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_post_urls(html_content):
    """Extract post URLs from the HTML content."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all anchor tags
        post_links = soup.find_all('a', href=True)
        # Filter links that contain '/status/' (commonly used in post URLs on X/Twitter)
        post_urls = [link['href'] for link in post_links if '/status/' in link['href']]
        # Ensure URLs are complete (prepend domain if necessary)
        post_urls = [f"https://x.com{url}" if url.startswith("/") else url for url in post_urls]
        return post_urls
    except Exception as e:
        print(f"Error extracting post URLs: {e}")
        return []

def save_to_excel(urls, file_name):
    """Save the list of URLs to an Excel file."""
    try:
        df = pd.DataFrame(urls, columns=['URL'])
        df.to_excel(file_name, index=False, engine='openpyxl')
        print(f"Data saved to {file_name}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")

def run_process():
    """Main process to download HTML, extract post URLs, and save to Excel."""
    input_url = "https://x.com/hashtag/Woxsen?src=hashtag_click"
    print(f"Fetching HTML content from {input_url}...")
    html_content = download_html(input_url)

    if html_content:
        print("Extracting post URLs...")
        post_urls = extract_post_urls(html_content)

        if post_urls:
            print(f"Extracted {len(post_urls)} post URLs.")
            save_to_excel(post_urls, "excel_file.xlsx")
        else:
            print("No post URLs found.")
    else:
        print("Failed to fetch or parse HTML content.")

# Run the process
if __name__ == "__main__":
    run_process()