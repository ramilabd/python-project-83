import requests
from bs4 import BeautifulSoup


def check_url(url):

    response = requests.get(url, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    h1_tag = soup.find('h1')
    title_tag = soup.find('title')
    description_tag = soup.find('meta', attrs={'name': 'description'})

    h1 = h1_tag.get_text(strip=True) if h1_tag else ''
    title = title_tag.get_text(strip=True) if title_tag else ''
    description = description_tag.get('content', '').strip() if description_tag else ''

    return {
        'status_code': response.status_code,
        'h1': h1[:255],
        'title': title[:255],
        'description': description[:255],
    }
