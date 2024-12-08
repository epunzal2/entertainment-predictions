import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url, headers=None) -> None:
        self.url = url
        self.headers = headers if headers else {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
        }
        self.soup = None
    
    def fetch_page(self):
        """
        Fetch the HTML content of the page and parse it with BeautifulSoup.
        """
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
            print("Page fetched successfully.")
        else:
            raise Exception(f"Failed to fetch page. Status code: {response.status_code}")
    
    def validate_soup(self):
        """
        Check if the page content has been fetched and parsed.
        """
        if not self.soup:
            raise Exception("No HTML content fetched. Call fetch_page() first.")
    
    def find_tables_with_attribute(self, attribute_name, attribute_value, report_count=False):
        """
        Find all tables with the given attribute name and value.
        """
        self.validate_soup()
        tables = self.soup.find_all('table', {attribute_name: attribute_value})
        if report_count:
            print(f"Found {len(tables)} tables with {attribute_name}={attribute_value}.")
        return tables
    
    def extract_table_data(self, table):
        pass

    def find_nearest_header(self, element, header_tags=('h1', 'h2', 'h3')):
        """
        Find the nearest preceding header for a given element.

        Args:
            element: The BeautifulSoup element to find the header for.
            header_tags: Tuple of header tags to search for (default: h1, h2, h3).

        Returns:
            str: The text of the nearest preceding header or None if no header is found.
        """
        header = element.find_previous(header_tags)
        return header.get_text(strip=True) if header else None

    def extract_categories_dict(self):
        pass
