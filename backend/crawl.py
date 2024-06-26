import yagooglesearch
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from fastapi import status, HTTPException

def searchGoogle(keyword: str, quantity: int) -> List[Dict[str, str]]:
    results = []
    seen_titles = set()
    client = yagooglesearch.SearchClient(
        keyword,
        tbs="qdr:d",
        lang_result="lang_vi",
        lang_html_ui="vi",
        max_search_result_urls_to_return=quantity,
        yagooglesearch_manages_http_429s=False,
        verbose_output=False,
    )
    client.assign_random_user_agent()

    urls = client.search()
    if "HTTP_429_DETECTED" in urls:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail='Hiện đang bị google chặn ip, hãy chờ 1 tiếng trước khi có thể crawl tiếp',
        )

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                title_element = soup.find('title')
                if not title_element:
                    continue

                title = title_element.text.strip()

                if title in seen_titles:
                    continue

                seen_titles.add(title)

                description_elements = soup.find_all('p')
                description = '\n'.join([paragraph.text.strip() for paragraph in description_elements])

                time_elements = [
                    soup.find('time'),
                    soup.find('span', class_='pdate'),
                    soup.find('span', class_='time'),
                    soup.find('span', class_='date'),
                    soup.find('span', class_='block-sc-publish-time'),
                    soup.find('div', attrs={'data-role': 'publishdate'}),
                    soup.find('div', class_='detail__meta')
                ]

                time = next((element.text.strip() for element in time_elements if element), 'Time not available')
                if time == 'Time not available':
                    continue

                results.append({'title': title, 'description': description, 'time': time, 'source': url})
        except Exception as e:
            print("An error occurred:", e)

    return results
