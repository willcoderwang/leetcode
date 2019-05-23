class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        res = []

        while sorted_deck:
            sorted_deck_pop = sorted_deck.pop()

            if not res:
                res.append(sorted_deck_pop)
            else:
                res_pop = res.pop()
                res.insert(0, res_pop)
                res.insert(0, sorted_deck_pop)

        return res