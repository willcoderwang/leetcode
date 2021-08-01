class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0

        tokens.sort()
        if power < tokens[0]:
            return 0

        head = 0
        head_sum = tokens[0]
        tail = len(tokens)
        tail_sum = power
        score = 1
        used = True

        while head < tail-1:
            if head_sum + tokens[head+1] <= tail_sum:
                head += 1
                head_sum += tokens[head]
                score += 1
                used = True
            else:
                tail -= 1
                tail_sum += tokens[tail]
                score -= 1
                used = False

        if not used:
            score += 1
        return score
