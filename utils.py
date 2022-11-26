import re
from config import Matches, Pattern, Results


class Utils:
    @staticmethod
    def find_urls_str(content: str) -> Results:
        regex: Pattern = re.compile(r"(<(.+) href\s?=\s?(['\"])(.*?)\3>.*</\2>)")
        matches: Matches = regex.findall(content)

        return list(map(lambda x: {'html': x[0], 'url': x[3]}, matches))
