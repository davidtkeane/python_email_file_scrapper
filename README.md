# python_email_file_scrapper
Web Scraper for Email Addresses

This Python script is a simple yet powerful tool for scraping email addresses from a given domain. It can be used for a variety of purposes, such as gathering contact information for outreach, research, or networking.

How It Works
The script works by sending a request to the domain's home page and extracting all the links found on the page. It then visits each link and scrapes any email addresses it finds. The script can also accept a CSV file with a list of URLs to scrape, allowing for batch processing of multiple pages at once.

The script saves the results in three CSV files, each prefixed with the domain name:

domain_name_email_list.csv: Contains all the email addresses found during the scraping process.
domain_name_links_found.csv: Contains all the links found on the domain's home page.
domain_name_url_search.csv: Contains the domain name or the list of URLs that were scraped.

Best way to Use the script!! 

1. run the script domain_email_file_scrape.py and select option 1 and search for the domain you want to scrape.
2. run the script domain_email_file_scrape.py again and chose option 2 and select the file that was saved example domain_links_found.csv and enter. 
    This will search all links found for any email address.
3. If you have your own list in .csv, select it and have one url on each line below each other.

# There is thane error message returned after running option 2 using a file, the script still works properly !

How to Run
To run the script, you'll need Python installed on your machine. You can then run the script from the command line using the following command: python script_name.py

Please replace script_name.py with the actual name of the script.

Note: Each time you run the script for a new domain, you'll need to change the domain name in the script.

Installation
Before running the script, you'll need to install the required Python libraries. You can do this by running the following command: pip install -r requirements.txt

This command should install all the necessary libraries, including requests, beautifulsoup4, tqdm, tkinter, and simpleaudio.

Future Improvements

While the script is fully functional as it is, there are several potential improvements that could be made:

Adding multi-threading or asynchronous functionality to speed up the scraping process.
Implementing more robust error handling to deal with potential issues such as network errors or changes in the structure of the target website.
Adding a graphical user interface (GUI) to make the script more user-friendly for those not comfortable with the command line.

Kind regards to you.

David
24-05-2023
