# Last updated: 5/25/2025, 9:29:35 PM
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counter = Counter(words)
        length = 0
        used_center = False

        for word in list(counter.keys()):
            rev = word[::-1]
            if word != rev:
                if rev in counter:
                    pairs = min(counter[word], counter[rev])
                    length += pairs * 4
                    counter[word] -= pairs
                    counter[rev] -= pairs
            else:
                pairs = counter[word] // 2
                length += pairs * 4
                counter[word] -= pairs * 2

        for word in counter:
            if word[0] == word[1] and counter[word] > 0:
                length += 2
                break

        return length
        