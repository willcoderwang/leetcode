class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return 0

        folder.sort()

        current = folder[0]
        result = [current]

        for f in folder[1:]:
            if len(f) >= len(current) and current == f[:len(current)] and f[len(current)] == '/':
                continue

            result.append(f)
            current = f

        return result