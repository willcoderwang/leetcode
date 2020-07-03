class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []
        for c in address:
            # print(c)
            if c == '.':
                result.extend('[.]')
            else:
                result.append(c)

        return ''.join(result)
