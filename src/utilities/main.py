

import os
import email
import justext
from scrapy.selector import Selector
import email
from email import policy

class CUtilities():

    def __init__(self):
        pass

    def extract_html_from_mhtml(self, file_path):
        with open(file_path, 'rb') as file:
            mhtml_content = file.read()
        
        message = email.message_from_bytes(mhtml_content, policy=policy.default)
        for part in message.walk():
            if part.get_content_type() == "text/html":
                return part.get_payload(decode=True).decode(part.get_content_charset())
        return None

    def parse_html_with_scrapy(self, html_content):
        # Use Scrapy's Selector for parsing
        selector = Selector(text=html_content)
        
        # Example: Extract all links
        links = selector.css('a::attr(href)').getall()
        
        # Example: Extract all text
        text = selector.css('body *::text').getall()
        
        return links, text
    
    def run_process(self, html_path):
        html_content = self.extract_html_from_mhtml(html_path)
        if html_content:
            links, text = self.parse_html_with_scrapy(html_content)
            print("Extracted Links:")
            print(links)
            print("\nExtracted Text:")
            print(text)
        else:
            print("No HTML content found in the MHTML file.")
        return links


# # Provide the path to your MHTML file
# mhtml_file_path = "path_to_your_file.mhtml"
# extracted_urls = extract_urls_from_mhtml(mhtml_file_path)

# # Display the extracted URLs
# print("Extracted URLs:")
# for url in extracted_urls:
#     print(url)
