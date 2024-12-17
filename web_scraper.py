import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch the HTML content of a webpage
def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to extract article titles and links
def extract_articles(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    articles = []
    
    # Assuming the articles are within <article> tags or specific class names (modify according to the target website)
    for article in soup.find_all('article'):
        title_tag = article.find('h2')  # Modify this based on the website's structure
        link_tag = article.find('a')
        
        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag.get('href')
            articles.append([title, link])
    
    return articles

# Function to write the extracted data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])  # Writing the header
        writer.writerows(data)  # Writing the data rows

# Main function
def main():
    url = input("Enter the URL of the website to scrape: ")  # For example, 'https://example.com/articles'
    
    # Fetch page content
    page_html = fetch_page(url)
    
    if page_html:
        # Extract articles from the page
        articles = extract_articles(page_html)
        
        if articles:
            # Save extracted data to a CSV file
            save_to_csv(articles, 'extracted_articles.csv')
            print(f"Extracted {len(articles)} articles and saved them to 'extracted_articles.csv'.")
        else:
            print("No articles found.")
    else:
        print("Failed to scrape the webpage.")

# Run the script
if __name__ == "__main__":
    main()
