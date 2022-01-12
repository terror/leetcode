class Solution:
  def isPalindrome(self, s: str) -> bool:
    # Remove non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s))

    i, j = 0, len(s) - 1
    while i < j:
      # If the ends don't match, it isn't a palindrome
      if s[i].lower() != s[j].lower():
        return False
      i += 1
      j -= 1

    return True
