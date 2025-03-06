
import requests
from bs4 import BeautifulSoup
import logging

def scrape_alternative_sources(original_text):
    """Searches the web for alternative perspectives on the given text."""
    search_query = f"https://www.google.com/search?q={'+'.join(original_text.split()[:10])}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(search_query, headers=headers)
        if response.status_code != 200:
            logging.error("Failed to retrieve search results")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if 'url?q=' in a['href']]
        
        alternative_texts = []
        for link in links[:5]:
            page = requests.get(link, headers=headers)
            if page.status_code == 200:
                page_soup = BeautifulSoup(page.text, 'html.parser')
                alternative_texts.append(page_soup.get_text())
        
        return alternative_texts
    except Exception as e:
        logging.error(f"Error scraping sources: {str(e)}")
        return []
def extract_article_text(url):
    """
    Extracts text content from an article page.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return ""
        
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        
        article_text = " ".join([p.get_text() for p in paragraphs])
        return article_text
    except Exception as e:
        print(f"Error extracting article text: {e}")
        return ""
