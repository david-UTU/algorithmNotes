import functools

word1 = input("First word:\n")
word2 = input("Second word:\n")

def levDist(word1, word2):
    @functools.lru_cache(None)
    def computeDist(word1_idx, word2_idx):
        if word1_idx < 0:
            return word2_idx + 1
        elif word2_idx < 0:
            return word1_idx + 1
        if word1[word1_idx] == word2[word2_idx]:
            return computeDist(word1_idx - 1, word2_idx -1)
        subLast = computeDist(word1_idx-1, word2_idx-1)
        addLast = computeDist(word1_idx, word2_idx-1)
        deleteLast = computeDist(word1_idx-1, word2_idx)
        return 1+min(subLast, addLast, deleteLast)
    return computeDist(len(word1)-1, len(word2)-1)

print(levDist(word1, word2))



