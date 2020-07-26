class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        the_map = self._get_the_map(order)

        for i in range(len(words)-1):
            if not self._compare(words[i], words[i+1], the_map):
                return False
        else:
            return True

    def _get_the_map(self, order):
        the_map = dict()
        for i, c in enumerate(order):
            the_map[c] = i

        return the_map

    def _compare(self, first, second, the_map):
        """
        returns True if first is less than or equals to second
        """
        if first == '':
            return True

        if second == '':
            return False

        for i in range(min(len(first), len(second))):
            if the_map[first[i]] < the_map[second[i]]:
                return True
            elif the_map[first[i]] > the_map[second[i]]:
                return False
        else:
            if len(first) <= len(second):
                return True
            else:
                return False