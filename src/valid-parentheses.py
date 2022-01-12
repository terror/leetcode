class Solution:
  def isValid(self, s: str) -> bool:
    delims = {'(': ')', '[': ']', '{': '}'}

    stack = []
    for c in s:
      if c in delims:
        stack.append(c)
      else:
        if not stack or delims[stack.pop()] != c:
          return False

    return len(stack) == 0
