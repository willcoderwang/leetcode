class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        d = digits[-1]
        result = []
        pre_results = self.letterCombinations(digits[:-1])
        if not pre_results:
            pre_results = ['']
        for r in pre_results:
            for c in mapping[d]:
                result.append(r+c)

        return result