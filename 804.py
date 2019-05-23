class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter2morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        result = []
        for word in words:
            num = 0
            for letter in word:
                for m in letter2morse[ord(letter) - ord('a')]:
                    num *= 2
                    if m == '-':
                       num += 1

            if num not in result:
                result.append(num)

        return len(result)