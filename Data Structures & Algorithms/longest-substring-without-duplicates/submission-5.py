class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        best = 0
        left = 0

        for right, char in enumerate(s):
            # If we see a repeating character inside the current window, move 'left' past it
            if char in char_idx and char_idx[char] >= left:
                left = char_idx[char] + 1

            # Store/update the most recent index of the character
            char_idx[char] = right

            # Calculate current window length and update max length
            best = max(best, right - left + 1)

        return best