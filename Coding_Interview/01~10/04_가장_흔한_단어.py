#가장 흔한 단어
#https://leetcode.com/problems/most-common-word

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pg: List(str) = re.sub('[^a-z]', ' ', paragraph.lower()).split()
        used_words: List(str) = []
        most_common: str = ""
        most_common_count: int = 0
        
        for word in pg:
            if (not word in used_words) and (not word in banned):
                used_words.append(word)
                count: int = pg.count(word)
                if count > most_common_count:
                    most_common_count = count
                    most_common = word
        
        return most_common
