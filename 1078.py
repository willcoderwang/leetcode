class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        results = []
        words = text.split()
        for index, word in enumerate(words):
            if word == first and index + 1 < len(words) and words[index + 1] == second and index + 2 < len(words):
                results.append(words[index + 2])

        return results
