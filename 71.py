class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        up_cnt = 0
        result = []
        for d in reversed(dirs):
            if not d or d == '.':
                continue
            elif d == '..':
                up_cnt += 1
                continue

            if up_cnt:
                up_cnt -= 1
                continue

            result.append(d)

        r = '/'.join(reversed(result))
        return '/' + r
