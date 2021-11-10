def compare(i1, i2):
    if i1[1] > i2[1]:
        return -1
    elif i1[1] == i2[1] and i1[0] <= i2[0]:
        return -1
    else:
        return 0


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = dict()
        for w in words:
            word_freq[w] = word_freq.get(w, 0) + 1

        word_list = list(word_freq.items())
        word_list.sort(key=functools.cmp_to_key(compare))
        return [i[0] for i in word_list[:k]]
