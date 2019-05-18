class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        pattern_norm = self.word_normalize(pattern)

        for word in words:
            if self.word_normalize(word, pattern_norm):
                res.append(word)

        return res

    def word_normalize(self, word, match=None):
        if match is not None and len(word) != len(match):
            return False

        res = []
        the_map = dict()
        i = 0
        for index, l in enumerate(word):
            map_res = the_map.get(l, None)
            if map_res is None:
                the_map[l] = i
                map_res = i
                i += 1

            res.append(map_res)

            if match is not None and map_res != match[index]:
                return False

        if match is None:
            return res
        else:
            return True