import csv
import os
import tempfile
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
from urllib.parse import urlparse, urljoin
import simpleaudio as sa
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import XMLParsedAsHTMLWarning
import time

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            links.append(href)
    return links

def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    emails = set()
    for email in soup.find_all('a', href=lambda href: href and 'mailto:' in href):
        emails.add(email['href'].split(':')[1])
    return emails

print('Please select a search option:')
print('1. Search using a URL')
print('2. Use a CSV file with URLs to scrape for email addresses')
search_option = input()

if search_option == '1':
    domain = input('Enter a URL to search: ')
else:
    root = tk.Tk()
    root.withdraw()
    urls_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select CSV file with URLs", filetypes=[("CSV files", "*.csv")])
    with open(urls_file, 'r') as f:
        urls = f.read().splitlines()
    domain = urlparse(urls[0]).scheme + '://' + urlparse(urls[0]).netloc

domain_name = urlparse(domain).netloc

home_page_links = get_links(domain)

contact_page_link = None
for link in home_page_links:
    if 'contact' in link.lower():
        contact_page_link = link
        break

if contact_page_link:
    contact_page_url = urljoin(domain, contact_page_link)
    contact_page_emails = extract_emails(contact_page_url)
else:
    contact_page_emails = set()

domain_emails = set()
if search_option == '1':
    links_to_scrape = home_page_links
else:
    links_to_scrape = urls

for link in tqdm(links_to_scrape, desc='Scraping pages', unit='page'):
    link_url = urljoin(domain, link)
    if urlparse(link_url).netloc == urlparse(domain).netloc:
        link_emails = extract_emails(link_url)
        domain_emails.update(link_emails)
    time.sleep(0.1)

with open(f'{domain_name}_email_list.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for email in tqdm(contact_page_emails | domain_emails, desc='Writing to file', unit='email'):
        writer.writerow([email])
        time.sleep(0.1)

with open(f'{domain_name}_links_found.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for link in home_page_links:
        writer.writerow([link])

with open(f'{domain_name}_url_search.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([domain])

audio_path = r'C:\Users\david\OneDrive\Projects_Mac\scripts-chat-ai\Wordpress+Web\webscrapping-works\audio\youve-got-mail-sound.wav'

if os.path.exists(audio_path):
    wave_obj = sa.WaveObject.from_wave_file(audio_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()
else:
    print('Audio file not found!')

print(contact_page_emails | domain_emails)

if search_option == '2':
    all_emails = set()
    for url in urls:
        url_emails = extract_emails(url)
        all_emails.update(url_emails)

    with open(f'{domain_name}_email_list.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for email in tqdm(all_emails, desc='Writing to file', unit='email'):
            writer.writerow([email])
            time.sleep(0.1)

    with open(f'{domain_name}_url_search.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([domain])

print('Scraping completed successfully!')
