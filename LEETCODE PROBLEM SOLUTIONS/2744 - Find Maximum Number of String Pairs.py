class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            if words[i][::-1] in (words[i + 1:]):
                result += 1
        return result
    