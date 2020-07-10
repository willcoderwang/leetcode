class Solution:
    def toGoatLatin(self, S: str) -> str:
        result = []
        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        for i, word in enumerate(S.split()):
            if word[0] in vowel:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'

            word += 'a' * (i + 1)
            result.append(word)

        return ' '.join(result)