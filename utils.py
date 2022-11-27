from config import Results, BeautifulSoup


class Utils:
    @staticmethod
    def find_urls_str(content: str) -> Results:
        soup: BeautifulSoup = BeautifulSoup(content, 'html.parser')
        results: Results = list(map(lambda a: {'html': str(a), 'url': a.get('href')}, soup.find_all('a', href=True)))

        return results
